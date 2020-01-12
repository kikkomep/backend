import shlex
import subprocess
import sys

from django.core.management.base import BaseCommand
from django.utils import autoreload


# https://stackoverflow.com/a/43929298/7364941
class Command(BaseCommand):
    def handle(self, *args, **options):
        autoreload.run_with_reloader(self._restart_celery)

    @classmethod
    def _restart_celery(cls):
        if sys.platform == "win32":
            cls.run('taskkill /f /t /im celery.exe')
            cls.run('celery worker --max-tasks-per-child 1 --loglevel=info --pool=solo -A backend')
        else:  # probably ok for linux2, cygwin and darwin. Not sure about os2, os2emx, riscos and atheos
            cls.run('pkill celery')
            cls.run('celery worker --max-tasks-per-child 1 -l info -A backend')

    @staticmethod
    def run(cmd):
        subprocess.call(shlex.split(cmd))

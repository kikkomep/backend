# Generated by Django 3.0.3 on 2020-02-24 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0011_add_celery_id_inference'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inference',
            options={},
        ),
        migrations.AlterModelOptions(
            name='modelweights',
            options={'verbose_name_plural': 'Model weights'},
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='ispretraining',
        ),
    ]
# Generated by Django 4.2.4 on 2023-09-23 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploaddata',
            old_name='resume',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='uploaddata',
            old_name='student',
            new_name='suser',
        ),
    ]

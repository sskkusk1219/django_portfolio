# Generated by Django 4.2.10 on 2024-11-19 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_cource_education_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='pampany',
            new_name='company',
        ),
    ]

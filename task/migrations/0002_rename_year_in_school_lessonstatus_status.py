# Generated by Django 4.2.5 on 2023-10-03 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonstatus',
            old_name='year_in_school',
            new_name='status',
        ),
    ]

# Generated by Django 3.2 on 2021-04-07 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='firest_name',
            new_name='first_name',
        ),
    ]

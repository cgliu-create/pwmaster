# Generated by Django 3.1.4 on 2020-12-02 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pwmanager', '0003_password_website'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PasswordGenerator',
        ),
    ]

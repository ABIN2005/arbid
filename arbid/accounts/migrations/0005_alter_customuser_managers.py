# Generated by Django 4.2.11 on 2024-04-19 08:59

import accounts.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', accounts.manager.UserManager()),
            ],
        ),
    ]

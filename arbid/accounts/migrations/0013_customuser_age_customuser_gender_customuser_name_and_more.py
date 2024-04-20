# Generated by Django 5.0.4 on 2024-04-19 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customuser_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'female')], default='m', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_bio',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('s', 'standard'), ('a', 'artist'), ('o', 'organisation')], default='', max_length=30),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-22 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_avatar_is_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='is_used',
        ),
    ]

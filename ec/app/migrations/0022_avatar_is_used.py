# Generated by Django 4.2.6 on 2023-11-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_rename_avatar_avatar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='is_used',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-14 09:24

import app.uploads
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_rename_customer_customeraddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_cat_name', models.CharField(max_length=100)),
                ('summary', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.uploads.upload_to_news_category)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Block', 'Block'), ('Active', 'Active')], default='Active', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'News Category',
                'verbose_name_plural': 'News Categories',
                'db_table': 'news_categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=100)),
                ('summary', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=app.uploads.upload_to_news)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('alias', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Block', 'Block'), ('Active', 'Active')], default='Active', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('news_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.news_category')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
            },
        ),
    ]
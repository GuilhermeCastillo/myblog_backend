# Generated by Django 5.0.1 on 2024-02-03 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='articles')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_tag', to='articles.tag')),
            ],
        ),
    ]

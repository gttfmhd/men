# Generated by Django 3.2.9 on 2021-12-14 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='наполнение')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='men.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Мужыки',
                'verbose_name_plural': 'Мужики',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
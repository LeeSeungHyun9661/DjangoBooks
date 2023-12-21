# Generated by Django 4.2.6 on 2023-12-20 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('personal_name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=50, null=True)),
                ('birth_date', models.CharField(max_length=100, null=True)),
                ('death_date', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_bestseller',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('olid', models.CharField(blank=True, max_length=20)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('authors', models.JSONField(default=dict, verbose_name='json')),
                ('publishers', models.CharField(blank=True, max_length=100, null=True)),
                ('publish_places', models.CharField(blank=True, max_length=100, null=True)),
                ('publish_date', models.CharField(blank=True, max_length=100, null=True)),
                ('languages', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('physical_format', models.CharField(blank=True, max_length=100, null=True)),
                ('physical_dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('subjects', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('preview_url', models.CharField(blank=True, max_length=200, null=True)),
                ('info_url', models.CharField(blank=True, max_length=200, null=True)),
                ('img_url_s', models.CharField(blank=True, max_length=200, null=True)),
                ('img_url_m', models.CharField(blank=True, max_length=200, null=True)),
                ('img_url_l', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'books',
            },
        ),
        migrations.CreateModel(
            name='NewRelease',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_new',
            },
        ),
    ]

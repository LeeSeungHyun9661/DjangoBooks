# Generated by Django 4.2.6 on 2023-12-14 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_subjects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-25 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBooks', '0003_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-SEQ_NO']},
        ),
    ]
# Generated by Django 4.2.6 on 2023-12-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_bestseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

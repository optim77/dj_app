# Generated by Django 4.0.2 on 2022-02-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0006_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]

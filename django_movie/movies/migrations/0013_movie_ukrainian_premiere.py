# Generated by Django 4.2.1 on 2023-06-01 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_movie_producer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ukrainian_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='Прем`єра в Україні'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20201228_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description_2',
            field=models.TextField(null=True, verbose_name='Докладний опис'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Стать', 'verbose_name_plural': 'Стать'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Відгук', 'verbose_name_plural': 'Відгуки'},
        ),
    ]
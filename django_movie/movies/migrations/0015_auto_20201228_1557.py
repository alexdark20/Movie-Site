# Generated by Django 4.2.1 on 2023-06-01 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20201227_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieshots',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movieshots', to='movies.movie', verbose_name='Фільм'),
        ),
    ]
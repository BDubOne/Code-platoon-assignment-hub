# Generated by Django 4.2.7 on 2023-11-21 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0003_alter_pokemon_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Unknown', validators=[django.core.validators.MinLengthValidator(7), django.core.validators.MaxLengthValidator(500)]),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

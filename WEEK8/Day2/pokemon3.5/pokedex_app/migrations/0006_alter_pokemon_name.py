# Generated by Django 4.2.7 on 2023-11-21 16:21

from django.db import migrations, models
import pokedex_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0005_alter_pokemon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=255, null=True, validators=[pokedex_app.validators.validate_name]),
        ),
    ]

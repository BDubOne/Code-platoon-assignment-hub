# Generated by Django 4.2.7 on 2023-11-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('move_app', '0001_initial'),
        ('pokedex_app', '0008_remove_trainer_pokedex_pokedex_trainer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(related_name='pokemon', to='move_app.move'),
        ),
    ]

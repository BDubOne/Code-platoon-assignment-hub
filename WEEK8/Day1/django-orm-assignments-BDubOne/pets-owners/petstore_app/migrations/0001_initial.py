# Generated by Django 4.2.7 on 2023-11-20 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='X', max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('vaccinated', models.BooleanField(default=False)),
                ('description', models.TextField(default='unknown')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('age', models.PositiveIntegerField(default=29)),
                ('number_of_pets', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='petstore_app.animal')),
                ('species', models.CharField(default='unknown')),
            ],
            bases=('petstore_app.animal',),
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='petstore_app.animal')),
                ('breed', models.CharField(default='unknown')),
            ],
            bases=('petstore_app.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='petstore_app.animal')),
                ('breed', models.CharField(default='unknown')),
            ],
            bases=('petstore_app.animal',),
        ),
        migrations.CreateModel(
            name='ExoticAnimal',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='petstore_app.animal')),
                ('region_of_origin', models.CharField(default='earth', max_length=250)),
                ('type_of_animal', models.CharField(max_length=100)),
            ],
            bases=('petstore_app.animal',),
        ),
    ]
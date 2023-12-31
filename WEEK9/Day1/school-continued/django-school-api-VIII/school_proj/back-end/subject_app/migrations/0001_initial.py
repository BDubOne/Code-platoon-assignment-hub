# Generated by Django 4.2.7 on 2023-11-29 21:36

from django.db import migrations, models
import subject_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(unique=True, validators=[subject_app.validators.validate_subject_format])),
                ('professor', models.CharField(validators=[subject_app.validators.validate_professor_name])),
            ],
        ),
    ]

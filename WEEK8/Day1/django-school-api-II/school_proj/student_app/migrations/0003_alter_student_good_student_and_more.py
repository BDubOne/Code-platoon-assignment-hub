# Generated by Django 4.2.7 on 2023-11-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_alter_student_personal_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='good_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(),
        ),
    ]
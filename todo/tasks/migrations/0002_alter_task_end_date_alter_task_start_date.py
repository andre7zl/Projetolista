# Generated by Django 4.2.7 on 2024-08-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(),
        ),
    ]

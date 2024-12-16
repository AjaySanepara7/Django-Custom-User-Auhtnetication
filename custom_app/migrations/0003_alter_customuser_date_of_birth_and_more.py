# Generated by Django 5.1.4 on 2024-12-13 11:55

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0002_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='hobby',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'Sports'), ('T', 'Travelling'), ('R', 'Reading'), ('P', 'Painting'), ('W', 'Writing')], max_length=9, null=True),
        ),
    ]
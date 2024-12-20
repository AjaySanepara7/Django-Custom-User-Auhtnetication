# Generated by Django 5.1.4 on 2024-12-16 06:31

import datetime
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_app', '0003_alter_customuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2024, 12, 16, 6, 31, 43, 759700, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='hobby',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'Sports'), ('T', 'Travelling'), ('R', 'Reading'), ('P', 'Painting'), ('W', 'Writing')], default='P', max_length=9),
        ),
    ]

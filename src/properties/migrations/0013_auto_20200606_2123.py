# Generated by Django 3.0.2 on 2020-06-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_property_information_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_information',
            name='small_thumbnail',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

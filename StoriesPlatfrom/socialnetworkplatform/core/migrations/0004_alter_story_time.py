# Generated by Django 4.1.7 on 2023-04-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_emailaddress_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.2.13 on 2023-02-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0025_associationteammembers_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionalbodiesteammembers',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.13 on 2023-01-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentServices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artsupdates',
            name='description',
        ),
        migrations.AddField(
            model_name='artsteamstatus',
            name='color',
            field=models.CharField(default='red-700', max_length=100),
        ),
        migrations.AddField(
            model_name='artsupdates',
            name='data',
            field=models.TextField(default='No data'),
        ),
        migrations.AlterField(
            model_name='artsteamstatus',
            name='lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artsteamstatus',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artsteamstatus',
            name='won',
            field=models.IntegerField(default=0),
        ),
    ]

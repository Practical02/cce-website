# Generated by Django 3.2.13 on 2022-12-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_alter_faculty_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevents',
            name='date',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.1.2 on 2021-06-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WIN', '0003_auto_20210620_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cBirthday',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]

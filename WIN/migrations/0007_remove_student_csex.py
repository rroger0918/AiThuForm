# Generated by Django 3.1.2 on 2021-06-19 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WIN', '0006_remove_student_cemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cSex',
        ),
    ]

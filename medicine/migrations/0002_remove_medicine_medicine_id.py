# Generated by Django 2.0.5 on 2018-09-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='medicine_id',
        ),
    ]

# Generated by Django 2.0.5 on 2018-09-25 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_auto_20180925_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicinepacket',
            old_name='expireing_date',
            new_name='expiring_date',
        ),
    ]

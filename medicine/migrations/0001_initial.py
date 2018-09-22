# Generated by Django 2.0.5 on 2018-09-22 22:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_id', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medicine_id', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Company')),
            ],
        ),
        migrations.CreateModel(
            name='MedicinePacket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('packet_id', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine')),
            ],
        ),
    ]

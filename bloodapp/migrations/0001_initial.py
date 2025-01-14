# Generated by Django 5.1 on 2024-08-27 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(db_index=True, null=True, upload_to='patient_image')),
                ('blood_type', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('age', models.IntegerField(db_index=True, null=True)),
                ('sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100)),
                ('email', models.CharField(db_index=True, max_length=200, null=True)),
                ('password', models.CharField(db_index=True, max_length=100, null=True)),
                ('phone', models.CharField(db_index=True, max_length=100, null=True)),
                ('address', models.TextField(db_index=True, null=True)),
                ('comment', models.TextField(db_index=True, null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

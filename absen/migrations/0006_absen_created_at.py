# Generated by Django 4.2.3 on 2023-08-31 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0005_alter_absen_mahasiswa'),
    ]

    operations = [
        migrations.AddField(
            model_name='absen',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
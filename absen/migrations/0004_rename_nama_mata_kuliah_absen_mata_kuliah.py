# Generated by Django 4.2.3 on 2023-08-31 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0003_absen_nama_mata_kuliah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='absen',
            old_name='nama_mata_kuliah',
            new_name='mata_kuliah',
        ),
    ]

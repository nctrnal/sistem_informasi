# Generated by Django 4.2.3 on 2023-09-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0005_alter_matakuliah_nama_mata_kuliah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Desain Web', 'Desain Web'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Sistem Informasi', 'Sistem Informasi'), ('Matematika Teknik', 'Matematika Teknik'), ('Struktur Data', 'Struktur Data')], max_length=100),
        ),
    ]

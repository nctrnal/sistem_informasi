# Generated by Django 4.2.3 on 2023-08-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0013_alter_matakuliah_nama_mata_kuliah_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Desain Web', 'Desain Web'), ('Matematika Teknik', 'Matematika Teknik'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Sistem Informasi', 'Sistem Informasi'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Struktur Data', 'Struktur Data')], max_length=100),
        ),
    ]

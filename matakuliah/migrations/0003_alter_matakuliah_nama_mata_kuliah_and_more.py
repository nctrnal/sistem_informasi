# Generated by Django 4.2.3 on 2023-08-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0002_alter_matakuliah_nama_mata_kuliah_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Matematika Teknik', 'Matematika Teknik'), ('Desain Web', 'Desain Web'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Struktur Data', 'Struktur Data'), ('Sistem Informasi', 'Sistem Informasi')], max_length=100),
        ),
        migrations.AlterField(
            model_name='matakuliah',
            name='tipe',
            field=models.CharField(blank=True, choices=[('Teori', 'Teori'), ('Praktikum', 'Praktikum')], default='', max_length=100),
        ),
    ]

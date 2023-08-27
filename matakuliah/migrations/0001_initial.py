# Generated by Django 4.2.3 on 2023-08-26 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dosen_pengajar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_mata_kuliah', models.CharField(max_length=10)),
                ('nama_mata_kuliah', models.CharField(choices=[('Matematika Teknik', 'Matematika Teknik'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Sistem Informasi', 'Sistem Informasi'), ('Desain Web', 'Desain Web'), ('Struktur Data', 'Struktur Data'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer')], max_length=100)),
                ('jumlah_sks', models.IntegerField()),
                ('program_studi', models.CharField(max_length=50)),
                ('tipe', models.CharField(blank=True, choices=[('Praktikum', 'Praktikum'), ('Teori', 'Teori')], default='', max_length=100)),
                ('kuota', models.IntegerField(blank=True, default=30)),
                ('kelas', models.CharField(default='A', max_length=100)),
                ('nama_pengajar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mata_kuliah_list', to='dosen_pengajar.dosenpengajarmodel')),
            ],
        ),
    ]

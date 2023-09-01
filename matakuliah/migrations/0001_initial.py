# Generated by Django 4.2.3 on 2023-08-30 08:46

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
                ('nama_mata_kuliah', models.CharField(choices=[('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Struktur Data', 'Struktur Data'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Sistem Informasi', 'Sistem Informasi'), ('Matematika Teknik', 'Matematika Teknik'), ('Desain Web', 'Desain Web')], max_length=100)),
                ('jumlah_sks', models.IntegerField(default=0)),
                ('program_studi', models.CharField(max_length=50)),
                ('tipe', models.CharField(blank=True, choices=[('Teori', 'Teori'), ('Praktikum', 'Praktikum')], default='', max_length=100)),
                ('kuota', models.IntegerField(blank=True, default=30)),
                ('kelas', models.CharField(default='A', max_length=100)),
                ('nama_pengajar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mata_kuliah_list', to='dosen_pengajar.dosenpengajarmodel')),
            ],
        ),
    ]

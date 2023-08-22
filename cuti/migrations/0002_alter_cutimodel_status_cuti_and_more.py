# Generated by Django 4.2.3 on 2023-08-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutimodel',
            name='status_cuti',
            field=models.CharField(choices=[('Status', 'Status'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Aktif', max_length=100),
        ),
        migrations.AlterField(
            model_name='cutimodel',
            name='tanggal_mulai',
            field=models.DateField(),
        ),
    ]

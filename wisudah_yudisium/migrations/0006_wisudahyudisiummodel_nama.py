# Generated by Django 4.2.3 on 2023-08-20 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_alter_mahasiswa_agama'),
        ('wisudah_yudisium', '0005_rename_toefle_wisudahyudisiummodel_toefl'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisudahyudisiummodel',
            name='nama',
            field=models.OneToOneField(default='nama', on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa'),
        ),
    ]

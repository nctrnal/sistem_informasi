# Generated by Django 4.2.3 on 2023-08-29 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0001_initial'),
        ('krs', '0006_mahasiswa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mahasiswa',
        ),
        migrations.AlterField(
            model_name='krs',
            name='mahasiswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa'),
        ),
    ]

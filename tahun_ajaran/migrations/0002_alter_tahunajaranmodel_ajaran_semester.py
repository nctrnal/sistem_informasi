# Generated by Django 4.2.3 on 2023-08-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tahun_ajaran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tahunajaranmodel',
            name='ajaran_semester',
            field=models.CharField(choices=[('Genap', 'Genap'), ('Ganjil', 'Ganjil')], max_length=100),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mahasiswa', models.CharField(max_length=100)),
                ('mata_kuliah', models.CharField(max_length=100)),
                ('status', models.CharField(default='belum di acc', max_length=20)),
            ],
        ),
    ]

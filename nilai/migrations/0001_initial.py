# Generated by Django 4.2.3 on 2023-08-29 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('krs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.DecimalField(decimal_places=2, max_digits=4)),
                ('krs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nilais', to='krs.krs')),
                ('matkul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krs.matakuliah')),
            ],
        ),
    ]

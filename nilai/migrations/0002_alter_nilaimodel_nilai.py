# Generated by Django 4.2.3 on 2023-08-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nilaimodel',
            name='nilai',
            field=models.CharField(blank=True, choices=[('E', 'E'), ('B', 'B'), ('D', 'D'), ('A', 'A'), ('C', 'C'), ('AB', 'AB'), ('BC', 'BC')], default='E', max_length=2),
        ),
    ]

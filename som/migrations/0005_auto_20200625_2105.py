# Generated by Django 3.0.7 on 2020-06-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('som', '0004_auto_20200625_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.DecimalField(choices=[(0.0, 'MASCULINO'), (1.0, 'FEMENINO')], decimal_places=1, max_digits=2, verbose_name='Sexo'),
        ),
    ]
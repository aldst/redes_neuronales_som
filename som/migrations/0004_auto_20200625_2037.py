# Generated by Django 3.0.7 on 2020-06-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('som', '0003_auto_20200625_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.IntegerField(choices=[(0.0, 'MASCULINO'), (1.0, 'FEMENINO')], verbose_name='Sexo'),
        ),
    ]

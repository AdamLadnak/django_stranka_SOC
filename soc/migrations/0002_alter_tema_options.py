# Generated by Django 4.2.13 on 2024-06-07 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['dostupnost'], 'verbose_name': 'Téma', 'verbose_name_plural': 'Témy'},
        ),
    ]
# Generated by Django 5.0 on 2024-06-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0003_dostupnost_alter_tema_dostupnost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='dostupnost',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Dostupnost',
        ),
    ]

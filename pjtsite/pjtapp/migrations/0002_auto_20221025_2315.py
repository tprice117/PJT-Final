# Generated by Django 3.2.13 on 2022-10-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjtapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printfiledata',
            name='FileTime',
            field=models.DecimalField(decimal_places=2, max_digits=48),
        ),
        migrations.AlterField(
            model_name='printfiledata',
            name='PrintTime',
            field=models.DecimalField(decimal_places=2, max_digits=48),
        ),
    ]

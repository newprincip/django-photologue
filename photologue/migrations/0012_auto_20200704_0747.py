# Generated by Django 3.0.7 on 2020-07-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=250, verbose_name='title'),
        ),
    ]

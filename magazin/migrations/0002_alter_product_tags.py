# Generated by Django 3.2.8 on 2021-10-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='magazin.Tag'),
        ),
    ]

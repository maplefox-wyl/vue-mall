# Generated by Django 2.2.9 on 2020-01-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(verbose_name='手机号'),
        ),
    ]

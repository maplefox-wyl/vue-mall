# Generated by Django 2.2.9 on 2020-01-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0002_auto_20200102_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='data',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, verbose_name='用户密码'),
        ),
    ]
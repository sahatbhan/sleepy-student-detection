# Generated by Django 3.2.6 on 2022-05-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20220503_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videomodel',
            name='date',
        ),
    ]
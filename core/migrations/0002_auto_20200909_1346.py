# Generated by Django 3.1.1 on 2020-09-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='closed_date',
            field=models.DateTimeField(null=True),
        ),
    ]
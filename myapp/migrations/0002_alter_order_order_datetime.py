# Generated by Django 4.0.5 on 2022-06-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.CharField(default='', max_length=200),
        ),
    ]

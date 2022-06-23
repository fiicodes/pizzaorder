# Generated by Django 4.0.5 on 2022-06-22 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_base_pizza_size_topping_pizzatopping_pizzaorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='topping_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.topping'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='pizzatopping',
        ),
    ]
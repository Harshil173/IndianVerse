# Generated by Django 4.0.6 on 2022-08-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210413_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TV', 'Television'), ('O', 'Other Items'), ('F', 'Fridge'), ('AC', 'Air Conditioner')], max_length=2),
        ),
    ]
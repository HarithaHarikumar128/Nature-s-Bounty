# Generated by Django 5.0.6 on 2024-07-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0009_remove_cartpayment_mycart_cartpayment_pdctdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartpayment',
            name='pdctdetails',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

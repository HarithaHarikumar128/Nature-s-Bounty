# Generated by Django 5.0.6 on 2024-08-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0024_frorder_deliverystatus_alter_cartpayment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='deliverystatus',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0015_alter_cartpayment_priceitm_alter_cartpayment_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartpayment',
            name='priceitm',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cartpayment',
            name='qty',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cartpayment',
            name='qtyprice',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

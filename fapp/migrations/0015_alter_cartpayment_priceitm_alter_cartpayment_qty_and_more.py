# Generated by Django 5.0.6 on 2024-07-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0014_alter_cartpayment_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartpayment',
            name='priceitm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartpayment',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cartpayment',
            name='qtyprice',
            field=models.IntegerField(default=0),
        ),
    ]

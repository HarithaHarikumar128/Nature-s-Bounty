# Generated by Django 5.0.6 on 2024-07-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0011_alter_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartpayment',
            name='farmer',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='cartpayment',
            name='fremail',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='cartpayment',
            name='priceitm',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='cartpayment',
            name='qty',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='cartpayment',
            name='qtyprice',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

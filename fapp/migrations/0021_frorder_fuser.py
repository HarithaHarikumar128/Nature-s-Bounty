# Generated by Django 5.0.6 on 2024-07-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0020_frorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='frorder',
            name='fuser',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]

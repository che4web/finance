# Generated by Django 5.0.2 on 2024-02-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_bankcard_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankcard',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
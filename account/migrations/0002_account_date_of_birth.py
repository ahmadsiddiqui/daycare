# Generated by Django 5.0.7 on 2025-01-22 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]

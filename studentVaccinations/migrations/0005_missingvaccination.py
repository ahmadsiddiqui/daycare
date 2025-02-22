# Generated by Django 5.0.7 on 2025-01-23 22:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentVaccinations', '0004_remove_vaccinationrecord_date_administered'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingVaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vaccination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentVaccinations.vaccination')),
            ],
        ),
    ]

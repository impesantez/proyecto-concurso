# Generated by Django 5.1.3 on 2024-12-01 22:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=30)),
                ('usage_hour', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
                ('usage_per_time', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carbon_footprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_hours', models.IntegerField(default=None, null=True)),
                ('monthly_times', models.IntegerField(default=None, null=True)),
                ('kwh', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('carbon', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='electricity.usage')),
            ],
        ),
    ]

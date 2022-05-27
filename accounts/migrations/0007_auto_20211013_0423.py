# Generated by Django 3.1.2 on 2021-10-13 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0004_auto_20211013_0143'),
        ('accounts', '0006_auto_20211013_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_by',
        ),
        migrations.AddField(
            model_name='healthregulator',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='health_regulator_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='healthregulator',
            name='store',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='businesses.store'),
        ),
    ]
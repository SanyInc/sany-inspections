# Generated by Django 3.1.2 on 2021-10-09 22:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('businesses', '0002_auto_20211010_0019'),
        ('accounts', '0001_initial'),
        ('checklists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Inspection unique identifier')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('inspector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.inspector', verbose_name='Inspector')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inspections', to='businesses.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Inspection',
                'verbose_name_plural': 'Inspections',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Complete',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('completed', models.DateTimeField(auto_now_add=True, verbose_name='Complete date')),
                ('score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('inspection', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='inspections.inspection', verbose_name='Inspection')),
            ],
            options={
                'verbose_name': 'Completed',
                'verbose_name_plural': 'Completed',
                'ordering': ('-completed',),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Choice')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Timpestamp')),
                ('comment', models.TextField(blank=True, default='-', verbose_name='Comment')),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='inspections.inspection', verbose_name='Inspection')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='checklists.question', verbose_name='Checklist Item')),
            ],
        ),
    ]
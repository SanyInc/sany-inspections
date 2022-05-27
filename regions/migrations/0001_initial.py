# Generated by Django 3.1.2 on 2021-10-09 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='RegionUnity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_unities', to='regions.region')),
            ],
            options={
                'verbose_name': 'Region Unity',
                'verbose_name_plural': 'Region Unities',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField()),
                ('region_unity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='regions.regionunity')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('slug', models.SlugField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zip_codes', to='regions.state')),
            ],
        ),
    ]
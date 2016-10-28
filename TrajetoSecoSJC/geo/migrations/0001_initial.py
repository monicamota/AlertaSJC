# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 10:57
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheia', models.DecimalField(db_index=True, decimal_places=2, max_digits=5)),
                ('observacao', models.CharField(max_length=254, null=True)),
            ],
            options={
                'ordering': ['cheia'],
                'verbose_name': 'Cota',
                'verbose_name_plural': 'Cotas',
            },
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=50)),
                ('codigo', models.IntegerField(db_index=True)),
                ('tipo', models.CharField(choices=[(b'mt', b'motorway'), (b'tk', b'trunk'), (b'pm', b'primary'), (b'sc', b'secondary'), (b'tt', b'tertiary'), (b'rd', b'residential'), (b'sv', b'service'), (b'un', b'unclassified')], max_length=4)),
                ('maounica', models.BooleanField(db_index=True)),
                ('sentido', models.CharField(max_length=2, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('referencia', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Logradouro',
                'verbose_name_plural': 'Logradouros',
            },
        ),
        migrations.AlterUniqueTogether(
            name='logradouro',
            unique_together=set([('nome', 'maounica')]),
        ),
        migrations.AddField(
            model_name='cota',
            name='logradouro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Logradouro'),
        ),
    ]
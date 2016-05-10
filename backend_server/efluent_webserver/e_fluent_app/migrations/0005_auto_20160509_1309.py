# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_fluent_app', '0004_patient_orthophoniste'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='orthophoniste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_fluent_app.Orthophoniste'),
        ),
        migrations.AddField(
            model_name='assignedexercise',
            name='exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_fluent_app.Exercise'),
        ),
        migrations.AddField(
            model_name='assignedexercise',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_fluent_app.Patient'),
        ),
    ]
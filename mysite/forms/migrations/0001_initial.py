# Generated by Django 4.0.5 on 2022-06-29 06:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('designation', models.CharField(max_length=50)),
                ('station', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('balance', models.PositiveSmallIntegerField(default=30)),
                ('prev_year_bal', models.PositiveSmallIntegerField(default=0)),
                ('entitlement', models.PositiveSmallIntegerField(default=0)),
                ('total_leave_days', models.PositiveSmallIntegerField(default=0)),
                ('days_taken', models.PositiveSmallIntegerField(default=0)),
                ('onleave', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.PositiveSmallIntegerField(default=0)),
                ('leave_type', models.TextField(max_length=20)),
                ('wef', models.DateField(default=datetime.date.today)),
                ('upto', models.DateField(default=datetime.date.today)),
                ('report_date', models.DateField(default=datetime.date.today)),
                ('approval_date', models.DateField(default=datetime.date.today)),
                ('assess_date', models.DateField(default=datetime.date.today)),
                ('others', models.TextField(blank=True)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('sup_code', models.PositiveIntegerField(default=0)),
                ('eo_code', models.PositiveIntegerField(default=0)),
                ('executive', models.CharField(default=0, max_length=50)),
                ('exec_comment', models.CharField(default=0, max_length=50)),
                ('substitute', models.CharField(default=0, max_length=50)),
                ('sub_code', models.CharField(default=0, max_length=50)),
                ('sub_job', models.CharField(default=0, max_length=50)),
                ('unit', models.CharField(default=0, max_length=50)),
                ('supervisor', models.CharField(default=0, max_length=50)),
                ('sup_comment', models.CharField(default=0, max_length=50)),
                ('Approved', models.BooleanField(default=False)),
                ('supervised', models.BooleanField(default=False)),
                ('assessed', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.staff')),
            ],
        ),
    ]

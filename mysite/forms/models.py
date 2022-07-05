from datetime import date
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, primary_key=True , on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    section = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    balance = models.PositiveSmallIntegerField(default=30)
    prev_year_bal = models.PositiveSmallIntegerField(default=0)
    entitlement = models.PositiveSmallIntegerField(default=0)
    total_leave_days = models.PositiveSmallIntegerField(default=0)
    days_taken = models.PositiveSmallIntegerField(default=0)
    onleave = models.BooleanField(default=False)


class Leave(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    days = models.PositiveSmallIntegerField(default=0)
    leave_type = models.TextField(max_length=20)
    wef = models.DateField(default=date.today)
    upto = models.DateField(default=date.today)
    report_date = models.DateField(default=date.today)
    approval_date = models.DateField(default=date.today)
    assess_date = models.DateField(default=date.today)
    others = models.TextField(blank=True)
    address = models.CharField(max_length=50)
    contact = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    sup_code = models.PositiveIntegerField(default=0)
    eo_code = models.PositiveIntegerField(default=0)
    executive = models.CharField(max_length=50, default=0)
    exec_comment = models.CharField(max_length=50, default=0)
    substitute = models.CharField(max_length=50, default=0)
    sub_code = models.CharField(max_length=50, default=0)
    sub_job = models.CharField(max_length=50, default=0)
    unit = models.CharField(max_length=50, default=0)
    supervisor = models.CharField(max_length=50, default=0)
    sup_comment = models.CharField(max_length=50, default=0)
    Approved = models.BooleanField(default=False)
    supervised = models.BooleanField(default=False)
    assessed = models.BooleanField(default=False)



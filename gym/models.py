from django.db import models
from datetime import date


class gym_website(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob=models.DateField(max_length=8)


class contact_detail(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=239)


   

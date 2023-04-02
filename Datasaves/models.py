from django.db import models
from datetime import date


class datasave(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=1024)
    dob=models.DateField(max_length=8)
    message = models.TextField()

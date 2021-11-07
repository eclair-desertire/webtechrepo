from typing import List
from django.conf import settings
from django.db import models
from django.utils import timezone

class TeamMember(models.Model):
    fullname=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=14)
    email=models.EmailField(max_length=200)
    office_hours=models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.fullname

class recipt(models.Model):
    rec_title=models.CharField(max_length=200)
    rec_desc=models.TextField()
    rec_main_image=models.ImageField()
    rec_ingredients=models.TextField()
    rec_receipt=models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.rec_title

# Create your models here.

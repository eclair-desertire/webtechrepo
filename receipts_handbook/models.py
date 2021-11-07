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

class Recipt(models.Model):
    rec_title=models.CharField(max_length=200)
    rec_desc=models.TextField()
    rec_main_image=models.ImageField(upload_to='receipts_handbook/models_files/main_images/',null=True)
    rec_lil_image=models.ImageField(upload_to='receipts_handbook/models_files/main_images/',null=True)
    rec_ingredients=models.TextField()
    rec_receipt=models.TextField()
    rec_category=models.CharField(max_length=200)
    rec_cooktime=models.CharField(max_length=200)
    rec_time_to_eat=models.CharField(max_length=200)
    # Recipt nutrirional values
    rec_calories=models.CharField(max_length=20)
    rec_protein=models.CharField(max_length=20)
    rec_fats=models.CharField(max_length=20)
    rec_carbs=models.CharField(max_length=20)
    def publish(self):
        self.save()

    def __str__(self):
        return self.rec_title

    def get_main_image_url(self):
        return self.rec_main_image.url.replace('receipts_handbook/','')

    def get_lil_image_url(self):
        return self.rec_lil_image.url.replace('receipts_handbook/','')
# Create your models here.

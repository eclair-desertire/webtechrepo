from django import forms
from django.db import models
from django.forms import fields
from .models import Recipt

class ReciptForm(forms.ModelForm):

    class Meta:
        model=Recipt
        fields=('rec_title','rec_desc',
        'rec_ingredients','rec_receipt','rec_category','rec_cooktime',
        'rec_time_to_eat','rec_calories','rec_protein','rec_fats','rec_carbs')
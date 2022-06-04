from django import forms
from django.db import models
from .models import CookieStand

class CreateAPIForm(forms.ModelForm):
    class Meta:
        model = CookieStand
        fields = [
            'location',
            'description',
            'hourly_sales',
            'minimum_customers_per_hour',
            'maximum_customers_per_hour',
            'average_cookies_per_sale',
            'description',
            ]

from django import forms
from django.db import models

class CreateAPIForm(forms.Form):
    location = models.CharField(max_length=256)
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    description = models.TextField(default="", null=True, blank=True)

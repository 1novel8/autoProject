import random

import factory.django
from django.db import models

from autoservice.enums import Brands, BodyTypes, FuelTypes
from customer.models import Customer
from autoProject.models import BaseModel


class Autoservice(BaseModel):
    name = models.CharField(max_length=30)
    feature_preference = models.JSONField()
    balance = models.IntegerField(default=0)
    car_catalog = models.ManyToManyField('Car', through='AutoserviceCarCatalog')
    sale_history = models.ManyToManyField(Customer, through='AutoserviceSaleHistory')


class Car(BaseModel):
    brand = models.CharField(max_length=30, choices=Brands.choices())
    body_type = models.CharField(max_length=30, choices=BodyTypes.choices())
    issue_year = models.IntegerField(default=0)
    model_of_car = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30, choices=FuelTypes.choices())
    mileage = models.IntegerField(default=0)


class AutoserviceCarCatalog(models.Model):
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='autoservice_car')
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)


class AutoserviceSaleHistory(models.Model):
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    date = models.DateTimeField(auto_created=True)

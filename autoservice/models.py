from django.db import models

from customer.models import Customer


class Autoservice(models.Model):
    name = models.CharField(max_length=30)
    feature_preference = models.JSONField()
    balance = models.IntegerField(default=0)
    car_catalog = models.ManyToManyField('Car', through='CarCatalog')
    sale_history = models.ManyToManyField(Customer, through='SaleHistory')


class Car(models.Model):
    brand = models.CharField(max_length=30)
    body_type = models.CharField(max_length=30)
    issue_year = models.IntegerField(default=0)
    model_of_car = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    mileage = models.IntegerField(default=0)


class CarCatalog(models.Model):
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)


class SaleHistory(models.Model):
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    cost = models.IntegerField(default=0)
    # date

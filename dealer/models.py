from django.db import models

from autoservice.models import Autoservice, Car, BaseModel


class Dealer(BaseModel):
    name = models.CharField(max_length=30)
    year_of_creation = models.IntegerField(default=0)
    sale_history = models.ManyToManyField(Autoservice, through='SaleHistory')
    car_catalog = models.ManyToManyField(Car, through='CarCatalog')
    count_of_buyers = models.IntegerField(default=0)


class SaleHistory(BaseModel):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL)
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)


class CarCatalog(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

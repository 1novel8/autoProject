from django.db import models

from autoservice.models import Autoservice, Car
from autoProject.models import BaseModel


class Dealer(BaseModel):
    name = models.CharField(max_length=30)
    year_of_creation = models.IntegerField(default=0)
    sale_history = models.ManyToManyField(Autoservice, through='DealerSaleHistory')
    car_catalog = models.ManyToManyField(Car, through='DealerCarCatalog')
    count_of_buyers = models.IntegerField(default=0)


class DealerSaleHistory(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    autoservice = models.ForeignKey(Autoservice, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_created=True)


class DealerCarCatalog(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)

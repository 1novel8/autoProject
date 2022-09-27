from django.db import models


class Customer(models.Model):
    balance = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    # email = models.EmailField()
    # password = models.CharField()

from django.db import models

from authorization.models import User
from autoProject.models import BaseModel


class Customer(BaseModel):
    balance = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

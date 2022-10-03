from django.db import models


class BaseModel(models.Model):
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_last_modification = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

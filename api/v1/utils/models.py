from django.db import models

# Create your models here.
class CustomAbstractModel(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

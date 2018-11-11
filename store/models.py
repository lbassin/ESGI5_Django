from django.db import models


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    cards_count = models.IntegerField()

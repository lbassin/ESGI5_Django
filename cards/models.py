from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    cardId = models.CharField(max_length=255, null=True)
    dbfId = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    cardSet = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255, null=True)
    playerClass = models.CharField(max_length=255, null=True)
    mechanics = models.CharField(max_length=255, null=True)
    faction = models.CharField(max_length=255, null=True)
    rarity = models.CharField(max_length=255, null=True)
    health = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    collectible = models.CharField(max_length=255, null=True)
    img = models.CharField(max_length=255, null=True)
    imgGold = models.CharField(max_length=255, null=True)
    isDefault = models.BooleanField(default=False)


class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card)

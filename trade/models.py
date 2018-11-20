from django.contrib.auth.models import User
from django.db import models

from cards.models import Card


class Trade(models.Model):
    user_source = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_source")
    user_target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_targer")
    cards_source = models.ManyToManyField(Card, related_name="cards_source")
    cards_target = models.ManyToManyField(Card, related_name="cards_target")
    credits_source = models.IntegerField()
    credits_target = models.IntegerField()

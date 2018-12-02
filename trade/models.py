from django.contrib.auth.models import User
from django.db import models

from cards.models import Card


class Trade(models.Model):
    WAITING_CODE = 0
    ACCEPTED_CODE = 1
    DECLINED_CODE = 2

    user_source = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_source")
    user_target = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_targer")
    cards_source = models.ManyToManyField(Card, related_name="cards_source")
    cards_target = models.ManyToManyField(Card, related_name="cards_target")
    credits_source = models.IntegerField()
    credits_target = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)

    def accept(self):
        self.status = self.ACCEPTED_CODE

    def decline(self):
        self.status = self.DECLINED_CODE

    def get_status_message(self):
        if self.status == self.ACCEPTED_CODE:
            return "Accepted"
        elif self.status == self.DECLINED_CODE:
            return "Declined"
        else:
            return "Waiting"

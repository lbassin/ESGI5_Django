from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from cards.models import Card, Deck
from hearthstone.settings import STARTUP_CREDITS


class ProfileManager(models.Manager):
    def create_profile(self, user):
        default_cards = Card.objects.filter(isDefault=True)

        profile = self.create(user=user)
        profile.cards.set(default_cards)

        return profile

    def get_decks(self, user):
        decks = Deck.objects.filter(user_id=user.id)

        return decks


class Profile(models.Model):
    objects = ProfileManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=STARTUP_CREDITS)
    cards = models.ManyToManyField(Card)
    following = models.ManyToManyField(User, name='following', related_name='followers')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create_profile(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

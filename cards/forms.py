from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from cards.models import Deck, Card
from hearthstone.settings import CARDS_BY_DECK


class CreateDeckForm(ModelForm):
    name = forms.CharField(max_length=255)
    user = forms.ModelChoiceField(User.objects, widget=forms.HiddenInput(), required=False)
    cards = forms.ModelMultipleChoiceField(Card.objects, widget=forms.SelectMultiple(attrs={'size': 20}))

    class Meta:
        model = Deck
        fields = ("name", "user", "cards")

    def clean_cards(self):
        value = self.cleaned_data['cards']
        if len(value) > CARDS_BY_DECK:
            raise forms.ValidationError("You can't select more than " + CARDS_BY_DECK.__str__() + " items.")
        return value

    def save(self, commit=True):
        deck = super().save(commit=False)
        deck.name = self.cleaned_data['name']
        deck.user = self.user
        deck.save()

        deck.cards.set(self.clean_cards())
        deck.save()

        return deck

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from cards.models import Deck, Card


class CreateDeckForm(ModelForm):
    name = forms.CharField(max_length=255)
    user = forms.ModelChoiceField(User.objects, widget=forms.HiddenInput(), required=False)
    cards = forms.ModelMultipleChoiceField(Card.objects)

    class Meta:
        model = Deck
        fields = ("name", "user", "cards")

    def save(self, commit=True):
        deck = super().save(commit=False)
        deck.name = self.cleaned_data["name"]

        if commit:
            deck.save()

        return deck

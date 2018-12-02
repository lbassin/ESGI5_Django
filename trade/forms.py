from pprint import pprint

from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList

from cards.models import Card
from trade.models import Trade


class CreateTradeForm(ModelForm):
    cards_source = forms.ModelMultipleChoiceField(Card.objects,
                                                  widget=forms.SelectMultiple(attrs={'size': 20}),
                                                  label="Cards",
                                                  required=False)
    cards_target = forms.ModelMultipleChoiceField(Card.objects,
                                                  widget=forms.SelectMultiple(attrs={'size': 20}),
                                                  label="Cards",
                                                  required=False)
    credits_source = forms.IntegerField(initial=0, label="Credits")
    credits_target = forms.IntegerField(initial=0, label="Credits")

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None,
                 user_source=None, user_target=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.user_source = user_source
        self.user_target = user_target

        self.fields['cards_source'].queryset = user_source.profile.cards.all()
        self.fields['cards_target'].queryset = user_target.profile.cards.all()

    class Meta:
        model = Trade
        fields = ("cards_target", "credits_target", "cards_source", "credits_source")

    def save(self, commit=True):
        trade = super().save(commit=False)
        trade.user_source_id = self.user_source.id
        trade.user_target_id = self.user_target.id
        trade.save()

        trade.cards_source.set(self.cleaned_data['cards_source'])
        trade.cards_target.set(self.cleaned_data['cards_target'])
        trade.save()

        return trade

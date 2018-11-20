from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList

from cards.models import Card
from trade.models import Trade


class CreateTradeForm(ModelForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None,
                 user_source=None, user_target=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.user_source = user_source
        self.user_target = user_target

    cards_source = forms.ModelMultipleChoiceField(Card.objects, widget=forms.SelectMultiple(attrs={'size': 20}))
    cards_target = forms.ModelMultipleChoiceField(Card.objects, widget=forms.SelectMultiple(attrs={'size': 20}))
    credits_source = forms.IntegerField()
    credits_target = forms.IntegerField()

    class Meta:
        model = Trade
        fields = ("cards_source", "cards_target", "credits_source", "credits_target")

    def save(self, commit=True):
        trade = super().save(commit=False)

        return trade

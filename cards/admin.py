# Register your models here.
import random

from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path

from cards import CardsManager
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'isDefault')
    change_list_template = "cards/changelist.html"
    ordering = ('-isDefault',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-api/', self.import_api),
        ]
        return my_urls + urls

    def import_api(self, request):
        if len(Card.objects.all()) <= 0:
            CardsManager.importCards().json()

            cards = list(Card.objects.all())
            for i in range(30):
                card = random.choice(cards)
                card.isDefault = True
                card.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# Register your models here.
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from cards import CardsManager
from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    change_list_template = "cards/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-api/', self.import_api),
        ]
        return my_urls + urls

    def import_api(self, request):
        if len(Card.objects.all()) <= 0:
            CardsManager.importCards().json()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

from django.contrib import admin

# Register your models here.
from trade.models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    pass

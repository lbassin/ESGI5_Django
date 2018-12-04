from django.contrib import admin

from forum.models import Topic, Message


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass

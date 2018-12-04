from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:25] + '...'

from pprint import pprint

from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList

from forum.models import Topic, Message


class CreateTopicForm(ModelForm):

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None,
                 user=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.user = user

    label = forms.CharField(max_length=255)

    class Meta:
        model = Topic
        fields = ("label",)

    def save(self, commit=True):
        topic = super().save(commit=False)
        topic.label = self.cleaned_data['label']
        topic.user_id = self.user.id

        topic.save()

        return topic


class CreateMessageForm(ModelForm):

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None,
                 user=None, topic=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

        self.user = user
        self.topic = topic

    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ("content",)

    def save(self, commit=True):
        message = super().save(commit=False)
        message.content = self.cleaned_data['content']
        message.topic_id = self.topic.id
        message.user_id = self.user.id

        message.save()

        return message

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from forum.forms import CreateTopicForm, CreateMessageForm
from forum.models import Topic


def index(request):
    topics = Topic.objects.order_by('-created_at')

    return render(request, 'forum/index.html', {'topics': topics})


@login_required
def create(request):
    form_topic = CreateTopicForm(request.POST if request.method == 'POST' else None, user=request.user)
    for key in form_topic.fields.keys():
        form_topic.fields[key].widget.attrs.update({'class': 'form-control'})

    form_message = CreateMessageForm(request.POST if request.method == 'POST' else None, user=request.user)
    for key in form_message.fields.keys():
        form_message.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        topic = form_topic.save()

        form_message.topic = topic
        form_message.save()

        return redirect('forum_view', id=topic.id)

    return render(request, 'forum/create.html', {'form_topic': form_topic, 'form_message': form_message})


def view(request, id):
    topic = Topic.objects.get(id=id)

    form = CreateMessageForm(request.POST if request.method == 'POST' else None, user=request.user, topic=topic)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        form.save()
        return redirect('forum_view', id=topic.id)

    messages = topic.message_set.order_by('created_at')

    return render(request, 'forum/view.html', {'topic': topic, 'messages': messages, 'form': form})

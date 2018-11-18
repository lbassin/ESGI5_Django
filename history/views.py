from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from history.models import History


@login_required
def home(request):
    following = request.user.profile.following.all()
    history = list()

    for user in following:
        history += History.objects.all().filter(user_id=user.id)

    pprint(history)

    return render(request, 'history/home.html', {'history': history})

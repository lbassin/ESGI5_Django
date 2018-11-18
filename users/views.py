from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect

from users.decorators import login_refused
from users.forms import UserCreationForm


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')


@login_refused
def register(request):
    form = UserCreationForm(request.POST if request.method == 'POST' else None)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('users_dashboard')

    return render(request, 'users/register.html', {'form': form})


@login_required
def users(request):
    users = User.objects.all()
    following = request.user.profile.following.all()

    return render(request, 'users/users_list.html', {'users': users, 'following': following})


@login_required
def cards(request, id):
    try:
        user = User.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'users/users_cards.html', {'cards': user.profile.cards.all(), 'user': user})


@login_required
def follow(request):
    try:
        target_user = User.objects.get(id=request.POST.get('id'))
    except ObjectDoesNotExist:
        raise Http404

    profile = request.user.profile
    profile.following.add(target_user)

    profile.save()

    return redirect('users_list')


@login_required
def unfollow(request):
    try:
        target_user = User.objects.get(id=request.POST.get('id'))
    except ObjectDoesNotExist:
        raise Http404

    profile = request.user.profile
    profile.following.remove(target_user)

    profile.save()

    return redirect('users_list')

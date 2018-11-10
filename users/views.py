from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cards.forms import CreateDeckForm
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

            return redirect('dashboard')

    return render(request, 'users/register.html', {'form': form})


@login_required
def cards(request):
    card_list = request.user.profile.cards.all()
    paginator = Paginator(card_list, 8)

    page = request.GET.get('page')
    cards = paginator.get_page(page)

    return render(request, 'users/cards.html', {'cards': cards})


@login_required
def decks(request):
    return render(request, 'users/decks.html')


@login_required
def decks_new(request):
    form = CreateDeckForm(request.POST if request.method == 'POST' else None)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        if form.is_valid():
            form.user = request.user
            deck = form.save()

    return render(request, 'users/decks_new.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cards.forms import CreateDeckForm
from users.models import Profile


@login_required
def cards(request):
    card_list = request.user.profile.cards.all()
    paginator = Paginator(card_list, 8)

    page = request.GET.get('page')
    displayed_card = paginator.get_page(page)

    return render(request, 'users/cards.html', {'cards': displayed_card})


@login_required
def decks(request):
    deck_list = Profile.object.get_decks(request.user)

    return render(request, 'users/decks.html', {'decks': deck_list})


@login_required
def decks_new(request):
    form = CreateDeckForm(request.POST if request.method == 'POST' else None)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        if form.is_valid():
            form.user = request.user
            form.save()

            return redirect('decks')

    return render(request, 'users/decks_new.html', {'form': form})

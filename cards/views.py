from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from cards.forms import CreateDeckForm
from cards.models import Deck, Card
from history.models import History
from users.models import Profile


@login_required
def cards(request):
    card_list = request.user.profile.cards.all()
    paginator = Paginator(card_list, 8)

    page = request.GET.get('page')
    displayed_card = paginator.get_page(page)

    return render(request, 'cards/cards.html', {'cards': displayed_card})


@login_required
def decks(request):
    deck_list = Profile.objects.get_decks(request.user)

    return render(request, 'cards/decks_list.html', {'decks': deck_list})


@login_required
def deck_new(request):
    form = CreateDeckForm(request.POST if request.method == 'POST' else None)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        if form.is_valid():
            form.user = request.user
            form.save()

            return redirect('decks')

    return render(request, 'cards/decks_new.html', {'form': form})


@login_required
def deck_edit(request, id):
    deck = Deck.objects.filter(id=id).get()
    form = CreateDeckForm(request.POST if request.method == 'POST' else None, instance=deck)

    if request.method == 'POST':
        if form.is_valid():
            form.user = request.user
            form.save()

            return redirect('decks')

    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    return render(request, 'cards/decks_edit.html', {'form': form})


@login_required
def deck_view(request, id):
    deck = Deck.objects.get(id=id)

    return render(request, 'cards/decks_view.html', {'deck': deck})


@login_required
def cards_view(request, id):
    card = Card.objects.get(id=id)

    return render(request, 'cards/cards_view.html', {'card': card})


@login_required
def cards_sell(request):
    try:
        profile = request.user.profile
        card = profile.cards.get(id=request.POST.get('id'))

        profile.cards.remove(card)
        profile.credits += 1

        history = History(user=request.user,
                          text="Sold the card '" + card.name + "'",
                          type='sell')
        history.save()

        profile.save()
    except ObjectDoesNotExist:
        return render(request, 'cards/cards_sell.html', {'success': False})

    return render(request, 'cards/cards_sell.html', {'success': True})

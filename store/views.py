# Create your views here.
from django.shortcuts import render

from cards.models import Card
from history.models import History
from store.models import Package


def store(request):
    packages = Package.objects.all()
    user_credits = request.user.profile.credits

    return render(request, 'store/store.html', {'packages': packages, 'user_credits': user_credits})


def buy(request):
    profile = request.user.profile
    package = Package.objects.get(id=request.POST.get('id'))
    if package.price > profile.credits:
        return render(request, 'store/buy.html', {'success': False})

    cards = Card.objects.get_random(package.cards_count)

    profile.cards.add(*cards)
    profile.credits -= package.price
    profile.save()

    history = History(user=request.user,
                      text="Bought a new pack of " + package.cards_count.__str__() + " cards",
                      type='store')
    history.save()

    return render(request, 'store/buy.html', {'success': True, 'package': package, 'cards': cards})

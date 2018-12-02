from pprint import pprint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from trade.forms import CreateTradeForm
from trade.models import Trade


@login_required
def trade(request, id):
    user_target = User.objects.get(id=id)
    user_source = request.user

    form = CreateTradeForm(request.POST if request.method == 'POST' else None,
                           user_source=user_source,
                           user_target=user_target)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('trade_index')

    return render(request, 'trade/new.html', {'user_target': user_target, 'user_source': user_source, 'form': form})


@login_required
def index(request):
    asking_trades = Trade.objects.filter(user_target_id=request.user.id).all()
    my_trades = Trade.objects.filter(user_source_id=request.user.id).all()

    return render(request, 'trade/list.html', {'my_trades': my_trades, "asking_trades": asking_trades})


@login_required
def view(request, id):
    trade = Trade.objects.get(id=id)

    return render(request, 'trade/view.html', {'trade': trade})

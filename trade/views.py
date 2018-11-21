from django.contrib.auth.models import User
from django.shortcuts import render

from trade.forms import CreateTradeForm


def trade(request, id):
    user_target = User.objects.get(id=id)
    user_source = request.user

    form = CreateTradeForm(request.POST if request.method == 'POST' else None,
                           user_source=user_source,
                           user_target=user_target)
    for key in form.fields.keys():
        form.fields[key].widget.attrs.update({'class': 'form-control'})

    return render(request, 'trade/trade.html', {'user_target': user_target, 'user_source': user_source, 'form': form})

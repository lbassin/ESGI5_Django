from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
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

            return redirect('dashboard')

    return render(request, 'users/register.html', {'form': form})

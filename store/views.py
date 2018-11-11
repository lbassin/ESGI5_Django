from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from store.models import Package


def store(request):
    packages = Package.objects.all()

    return render(request, 'store/store.html', {'packages': packages})

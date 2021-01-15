from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    context = {'name': 'Black'}
    return render(request, 'home.html', context)





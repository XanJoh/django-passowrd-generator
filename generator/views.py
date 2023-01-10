from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thePassword = ''
    charactersList = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactersList.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        charactersList.extend(list('!@#$%&*'))

    if request.GET.get('numbers'):
        charactersList.extend(list('123456789'))

    length = int(request.GET.get('length',12)) #12 will be the default if nothing is passed
    for x in range(length):
        thePassword += random.choice(charactersList)

    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')
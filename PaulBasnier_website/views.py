from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html', {'date': datetime.datetime.now()})


def current_datetime(request, pseudo):
    now = datetime.datetime.now()
    return render(request, 'datetime.html', locals())


from django.shortcuts import render
from .models import Sity, News, Test_kz

def index(request):
    sities = Sity.objects.all()


    return render(request, 'App_kz/index.html', {"sities": sities})

def about(request):
    news = News.objects.all()
    return render(request, 'App_kz/about.html', {"news": news})
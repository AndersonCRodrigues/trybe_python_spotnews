from django.shortcuts import render
from news.models import News

# Create your views here.


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})

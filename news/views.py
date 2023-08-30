from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from news.form.forms import CategoryForm

# Create your views here.


def home(request):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news": news})


def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = CategoryForm()

    return render(request, "categories_form.html", {"form": form})

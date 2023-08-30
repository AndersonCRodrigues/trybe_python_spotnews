from django.urls import path
from news.views import home, category_form, news_details

urlpatterns = [
    path("", home, name="home-page"),
    path('news/<int:id>/', news_details, name='news-details-page'),
    path('categories/', category_form, name='categories-form'),
]

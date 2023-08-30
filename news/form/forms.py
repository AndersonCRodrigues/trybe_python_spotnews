from django import forms
from news.models import Categories, News


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label="Nome", max_length=200)

    class Meta:
        model = Categories
        fields = ["name"]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]

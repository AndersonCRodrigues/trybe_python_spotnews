from django.db import models
from news.models.user_model import Users
from news.models.category_model import Categories
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError(("O título deve conter mais de uma palavra."))


def validate_date_format(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")

        return True
    except ValueError as e:
        raise ValidationError(
            "Use o formato AAAA-MM-DD e uma data igual ou anterior a hoje."
        ) from e


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, validators=[validate_title]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField(validators=[validate_date_format])
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

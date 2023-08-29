from django.db import models
from news.models.user_model import Users
from news.models.category_model import Categories
from django.core.exceptions import ValidationError


def validate(value):
    words = len(value.split())

    if words < 2:
        raise ValidationError("O título deve conter pelo menos 2 caracteres.")


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, validators=[validate]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

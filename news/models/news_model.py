from django.db import models
from news.models.user_model import Users
from news.models.category_model import Categories
from django.core.exceptions import ValidationError


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError(("O título deve conter mais de uma palavra."))


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, validators=[validate_title]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

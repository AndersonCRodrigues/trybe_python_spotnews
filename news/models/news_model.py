from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


def validate_title(value):
    if len(value.split()) < 2:
        raise ValidationError(("O título deve conter pelo menos 2 palavras."))


def validate_date_format(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")

        return True
    except ValueError:
        raise ValidationError(
            "Use o formato AAAA-MM-DD."
        )


class News(models.Model):
    title = models.CharField(
        max_length=200, null=False, validators=[validate_title]
    )
    content = models.TextField(null=False)
    author = models.ForeignKey("Users", on_delete=models.CASCADE)
    created_at = models.DateField(validators=[validate_date_format])
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title

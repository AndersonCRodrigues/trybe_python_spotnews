# Generated by Django 4.2.3 on 2023-08-29 23:13

from django.db import migrations, models
import django.db.models.deletion
import news.models.news_model


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=200,
                        validators=[news.models.news_model.validate_title],
                    ),
                ),
                ("content", models.TextField()),
                (
                    "created_at",
                    models.DateField(
                        validators=[
                            news.models.news_model.validate_date_format
                        ]
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="img/"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.users",
                    ),
                ),
                ("categories", models.ManyToManyField(to="news.categories")),
            ],
        ),
    ]

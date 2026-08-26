from django.db import models
from django.db.models import Q


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="Назва")
    city = models.CharField(max_length=80, blank=True, default="", verbose_name="Місто")
    founded_year = models.PositiveSmallIntegerField(null=True, blank=True)
    site = models.URLField(blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Видавництво"
        verbose_name_plural = "Видавництва"


class Genre(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=120, unique=True)
    email = models.EmailField(blank=True, default="")
    country = models.CharField(max_length=60, blank=True, default="")
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft"
        PUBLISHED = "published"
        ARCHIVED = "archived"
        DAMAGED = "damaged"

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, default="")
    slug = models.SlugField(max_length=200, unique=True)
    isbn = models.CharField(max_length=17, unique=True, db_index=True)
    summary = models.TextField(blank=True, default="")

    authors = models.ManyToManyField(Author, related_name="books")
    genres = models.ManyToManyField(Genre, blank=True, related_name="books")
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )

    pages = models.PositiveSmallIntegerField(null=True, blank=True)
    extra_info = models.JSONField(default=dict, blank=True)

    status = models.CharField(max_length=10, choices=Status, default=Status.DRAFT)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["status", "-updated_at"])]
        constraints = [
            models.CheckConstraint(condition=~Q(title=""), name="book_title_not_empty")
        ]
        permissions = [("can_publish_book", "Can publish books")]


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"

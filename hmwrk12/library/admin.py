from django.contrib import admin

from .models import Author, Book, Genre, Publisher, Movie


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "authors_list",
        "publisher",
        "status",
        "isbn",
        "updated_at",
        "created_at",
    )
    list_display_links = ("title", "isbn")
    list_editable = ("status",)

    ordering = ("title",)
    sortable_by = ("isbn", "publisher")

    list_per_page = 10
    list_max_show_all = 55

    empty_value_display = r"¯\_(ツ)_/¯"

    list_filter = (
        "status",
        ("publisher", admin.RelatedOnlyFieldListFilter),
        "updated_at",
        "created_at",
    )

    search_fields = ("title", "isbn")

    fields = (("title", "subtitle"), ("status", "publisher"))

    def authors_list(self, obj):
        my_authors = obj.authors.all()
        return ", ".join(a.full_name for a in my_authors) if my_authors else "--"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin): ...


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin): ...


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin): ...


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "year", "genre", "rating")
    list_display_links = ("title",)
    list_editable = ("rating",)

    ordering = ("title",)

    list_filter = ("genre", "year")

    search_fields = ("title", "director")

    list_per_page = 10

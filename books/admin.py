from typing import ClassVar

from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = [
        "title",
        "author",
        "description",
        "price",
        "publisher",
        "pubdate",
    ]
    search_fields: ClassVar[list[str]] = ["title", "author"]
    ordering: ClassVar[list[str]] = ["title", "author"]
    inlines: ClassVar[list[str]] = [
        ReviewInline,
    ]


admin.site.register(Review)


class ReviewAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["review", "date", "creator"]
    search_fields: ClassVar[list[str]] = ["creator", "review"]

from django.urls import path

from .views import (
    BookCreateView,
    BookDetailView,
    BookListView,
    SearchResultsListView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add/", BookCreateView.as_view(), name="book_add"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]

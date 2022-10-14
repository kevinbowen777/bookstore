from django.urls import path

from .views import (
    BookCreateView,
    BookDetailView,
    BookListView,
    BookUpdateView,
    ReviewCreateView,
    ReviewDeleteView,
    ReviewDetailView,
    SearchResultsListView,
)

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add/", BookCreateView.as_view(), name="book_add"),
    path("<uuid:pk>/update/", BookUpdateView.as_view(), name="update"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path(
        "<uuid:pk>/review/add/",
        ReviewCreateView.as_view(),
        name="review_create",
    ),
    path("review/<int:pk>/", ReviewDetailView.as_view(), name="review_detail"),
    path(
        "review/<int:pk>/delete/",
        ReviewDeleteView.as_view(),
        name="review_delete",
    ),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]

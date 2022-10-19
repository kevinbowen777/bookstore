from django.urls import reverse
from django.test import RequestFactory  # noqa:F401
import pytest
from pytest_django.asserts import (
    assertContains,
)

from .factories import BookFactory
from ..models import Book
from ..views import (
    BookCreateView,
    BookDetailView,
    BookListView,
)


pytestmark = pytest.mark.django_db


def test_book_list_view(rf):
    # Get the request
    request = rf.get(reverse("book_list"))
    # Use the request to get the response
    response = BookListView.as_view()(request)
    # Test that the response is valid
    assertContains(response, "Our Book list")


def test_book_list_contains_2_books(rf):
    # Create a couple of books
    book1 = BookFactory()
    book2 = BookFactory()
    # Create a request and then a response
    # for the list of books
    request = rf.get(reverse("book_list"))
    response = BookListView.as_view()(request)
    # Assert that the response contains both book titles
    # in the template
    assertContains(response, book1.title)
    assertContains(response, book2.title)


def test_book_detail_view(rf):
    # Order a book from the BookFactory
    book = BookFactory()
    # Get the request
    url = reverse("book_detail", kwargs={"pk": book.pk})
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = BookDetailView.as_view()
    response = callable_obj(request, pk=book.pk)
    # Test that the response is valid
    assertContains(response, book.title)


def test_detail_contains_book_data(rf):
    book = BookFactory()
    # Make a request for our new book
    url = reverse("book_detail", kwargs={"pk": book.pk})
    request = rf.get(url)
    # Use the request to get the response
    callable_obj = BookDetailView.as_view()
    response = callable_obj(request, pk=book.pk)
    # Test our Book details:
    assertContains(response, book.title)
    assertContains(response, book.author)
    assertContains(response, book.price)


def test_book_create_form_valid(rf, admin_user):
    # Submit the book add form
    form_data = {
        "title": "Programming Python",
        "author": "Mark Lutz",
        "price": "69.00",
    }
    request = rf.post(reverse("book_add"), form_data)
    request.user = admin_user
    response = BookCreateView.as_view()(request)  # noqa:F841
    # Get the book based on the name
    book = Book.objects.get(title="Programming Python")  # noqa:F811
    # Test that the book matches our form
    assert book.author == "Mark Lutz"
    assert book.price == 69.00
    assert book.creator == admin_user


"""
def test_review_create_form_valid(rf, admin_user):
    # Submit the book add form
    book = BookFactory()
    form_data = {
        # "book": str(book.id),
        "review": "This is a great book",
    }
    url = reverse("review_create", kwargs={'pk': book.pk})
    request = rf.post(url, form_data)
    request.user = admin_user
    response = ReviewCreateView.as_view()(request)  # noqa:F841
    # Get the book based on the name
    review = Review.objects.get(review="This is a great book")  # noqa:F811
    # Test that the book matches our form
    assert review.book == book.title
    assert review.review == "This is a great book"
    assert review.creator == admin_user
"""

import pytest
from django.test import Client, RequestFactory

from accounts.tests.factories import UserFactory
from books.models import Book
from books.tests.factories import BookFactory, ReviewFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def request_factory():
    return RequestFactory()


@pytest.fixture
def book():
    return BookFactory()


@pytest.fixture
def review():
    return ReviewFactory()


@pytest.fixture
def client():
    return Client()


# Create posts for pagination tests
@pytest.fixture
def ten_books(user):
    books = []
    for book_id in range(10):
        book_id += 1
        Book.objects.create(
            title="A Tiny Test Bookstore Post {0}".format(book_id),
            author=user,
            price=19.95,
            publisher="Grove Press",
            # tags="dummy, test, django, bookstore",
            # slug="2023/9/18/a-tiny-bookstore-test-{0}/".format(book_id),
            description="Some bookstore content {0}".format(book_id),
        )
        books.append(book)
    return books

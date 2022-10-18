from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.test import RequestFactory  # noqa:F401
import pytest

from ..models import Book, Review
from ..views import (
    BookCreateView,
)

pytestmark = pytest.mark.django_db


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )
        self.special_permission = Permission.objects.get(
            codename="special_status"
        )
        self.book = Book.objects.create(
            title="Learning Python",
            author="Mark Lutz",
            price="53.00",
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review="An excellent review",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Learning Python")
        self.assertEqual(f"{self.book.author}", "Mark Lutz")
        self.assertEqual(f"{self.book.price}", "53.00")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learning Python")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, "%s?next=/books/" % (reverse("account_login"))
        )
        response = self.client.get(
            "%s?next=/books/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Learning Python")
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "An excellent review")


# def test_book_create_form_valid(rf):
def test_book_create_form_valid(rf, admin_user):
    # Submit the book add form
    form_data = {
        "title": "Programming Python",
        "author": "Mark Lutz",
        "price": "69.00",
    }
    request = rf.post(reverse("book_add"), form_data)
    # request.user = self.user
    request.user = admin_user
    response = BookCreateView.as_view()(request)  # noqa:F841
    # Get the book based on the name
    book = Book.objects.get(title="Programming Python")  # noqa:F811
    # Test that the book matches our form
    assert book.author == "Mark Lutz"
    assert book.price == 69.00
    # assert book.creator == self.user
    assert book.creator == admin_user

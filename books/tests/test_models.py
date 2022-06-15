from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase

from ..models import Book, Review


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

    def test__str__(self):
        assert self.book.__str__() == self.book.title
        assert str(self.book) == self.book.title

    def test_get_absolute_url(self):
        url = self.book.get_absolute_url()
        assert url == f"/books/{self.book.id}/"

    def test_review__str__(self):
        assert self.review.__str__() == self.review.review
        assert str(self.review) == self.review.review

    def test_review_get_absolute_url(self):
        url = self.review.get_absolute_url()
        assert url == f'{"/books/"}'

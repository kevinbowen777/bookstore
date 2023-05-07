from django.test import TestCase

from accounts.tests.factories import UserFactory

from ..models import Review
from .factories import BookFactory


class BookTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.book = BookFactory()
        self.review = Review.objects.create(
            book=self.book,
            creator=self.user,
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

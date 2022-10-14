from accounts.tests.factories import UserFactory
import factory
import factory.fuzzy

from ..models import Book


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    author = factory.SubFactory(UserFactory)
    price = factory.fuzzy.FuzzyDecimal(low=9.95, high=99.99)
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Book

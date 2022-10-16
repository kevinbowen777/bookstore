from accounts.tests.factories import UserFactory
import factory
import factory.fuzzy

from ..models import Book


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="The Book of ")
    author = factory.SubFactory(UserFactory)
    price = factory.fuzzy.FuzzyDecimal(low=9.95, high=99.99)
    creator = factory.SubFactory(UserFactory)

    class Meta:
        model = Book

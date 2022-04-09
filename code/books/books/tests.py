from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='Learning Python',
            author='Mark Lutz',
            price='53.00',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Learning Python')
        self.assertEqual(f'{self.book.author}', 'Mark Lutz')
        self.assertEqual(f'{self.book.price}', '53.00')

    def test_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Learning Python')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Learning Python')
        self.assertTemplateUsed(response, 'books/book_detail.html')

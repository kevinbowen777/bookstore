from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "price", "cover"]
    template_name = "books/book_add.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

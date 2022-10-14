from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy  # noqa: F401
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Book, Review


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"

    paginate_by = 10


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


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "author", "price", "cover"]
    template_name = "books/book_add.html"
    action = "Update"


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "reviews/review_create.html"
    fields = ["book", "review"]

    def get_initial(self):
        initial_data = super(ReviewCreateView, self).get_initial()
        book = Book.objects.get(id=self.kwargs["pk"])
        initial_data["book"] = book
        return initial_data

    def get_context_data(self):
        context = super(ReviewCreateView, self).get_context_data()
        book = Book.objects.get(id=self.kwargs["pk"])
        context["book"] = book
        context["title"] = "Add a new review"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    """
    def get_success_url(self):
        book = Book.objects.get(id=self.kwargs["pk"])
        return reverse("book_detail", args=[self.object.pk])
    """


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    context_object_name = "review"
    template_name = "reviews/review_detail.html"


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ["book", "review"]
    template_name = "reviews/review_update.html"
    action = "Update"


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "reviews/review_delete.html"
    success_url = reverse_lazy("book_list")


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

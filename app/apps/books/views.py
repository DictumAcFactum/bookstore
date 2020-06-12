from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book

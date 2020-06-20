from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    login_url = 'account_login'
    permission_required = 'books.special_status'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('review_set')

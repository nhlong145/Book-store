from django.shortcuts import render

# Create your views here.
# books/views.py
from django.contrib.auth.mixins import (
LoginRequiredMixin,
PermissionRequiredMixin # new
)
from django.views.generic import ListView, DetailView # new
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list' # new
    template_name = 'books/book_list.html'
    login_url = 'account_login' # new


class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView): # new
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'
    login_url = 'account_login' # new
    permission_required = 'books.special_status' # new
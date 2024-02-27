from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .form import *
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book-list.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(DetailView):
    model = Book
    template_name = "book-detail.html"
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    class_form = BookForm
    template_name = 'book-create.html'
    fields = ['title', 'author', 'price', 'publisher', 'image']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    class_form = BookForm
    template_name = 'book-update.html'
    fields = ['title', 'price', 'publisher', 'image']
    success_url = reverse_lazy('book-list') 

class BookDeleteView(DeleteView):
    model = Book
    class_form = BookForm
    template_name = 'book-delete.html'
    success_url = reverse_lazy('book-list')


@require_POST
def email_send(request):
    subject = request.POST['name']
    message = request.POST['message']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mamajonovibrokhimjon@gmail.com']
    send_mail(subject, message, email_from, recipient_list )
    return render(request, 'book-list.html')
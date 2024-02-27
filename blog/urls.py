from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book-create/', BookCreateView.as_view(), name='book-create'),
    path('book-update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('content/', email_send, name='content'),
]
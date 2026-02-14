from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:id>', views.books),
    path('add_author_to_book', views.add_author_to_book),
    path('delete_book_by_id', views.delete_book_by_id),


    path('authors', views.authors_page),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.authors),
    path('add_book_to_author', views.add_book_to_author),
    path('delete_author_by_id', views.delete_author_by_id),
]
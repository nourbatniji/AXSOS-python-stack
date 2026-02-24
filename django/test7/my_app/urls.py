from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_user', views.create_user),
    path('login_user', views.login_user),
    path('books', views.books_page),
    path('logout', views.logout),
    path('books/add', views.add_book_pg),
    path('add_book', views.create_book),
]
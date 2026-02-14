from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('reg_user', views.register_user), 
    path('login_user', views.login_user), 
    path('logout', views.logout_user), 
    path('books_home', views.books_home), 
    path('go_add_book', views.add_book_page), 
    path('add_book', views.add_book), 
    path('books/<int:id>', views.book_details), 
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_user', views.reg_user),   #do signup
    path('login_user', views.login_user),   #do login
    path('books', views.books),   #home page
    path('add_fav_book', views.add_fav_book),
    path('books/<int:id>', views.book_details),
    path('update_book', views.update_book),
    path('delete_book', views.delete_book),
    path('add_book_to_user_likes', views.add_book_to_user_likes),
    path('delete_book_from_fav', views.delete_book_from_fav),
    path('logout', views.logout),
]
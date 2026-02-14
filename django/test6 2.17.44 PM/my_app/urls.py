
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_user', views.create_user),
    path('login_user', views.login_user),
    path('books', views.books_page),
    path('logout', views.logout),
]

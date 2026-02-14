from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.signup_page), #display signup page
    path('sign_up', views.sign_up), #do the signup
    path('signin', views.signin_page), #display signin page
    path('sign_in', views.sign_in), #do the sign in
    path('users/new', views.new_user_page), #display new users dashboard
    path('create_new_user', views.sign_up), #display new users dashboard
    path('dashboard', views.display_all_users), #do the sign in
]
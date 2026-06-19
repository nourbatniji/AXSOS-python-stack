from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('go_to_signup', views.signup_page), #display sign up page
    path('signup', views.sign_up), #do the sign up 
    path('go_to_login', views.login_page), #display sign in page
    path('login', views.log_in), #do the sign in 
    path('homepage', views.home_page),
    path('users', views.users_page),
    path('user_details/<int:id>', views.user_details),
    path('sign_out', views.sign_out),
    path('delete_user', views.delete_user),
    path('update_page/<int:id>', views.update_page),
    path('edit/<int:id>', views.edit_user),
    path('addresses/<int:id>', views.address_page),
    path('add_address', views.add_address),
    path('user_addresses/<int:id>', views.user_addresses_page),
]
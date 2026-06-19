from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_user', views.reg_user),
    path('login_user', views.login_user),
    path('success/<int:id>', views.success, name='success'),
    path('log_out', views.log_out),

]
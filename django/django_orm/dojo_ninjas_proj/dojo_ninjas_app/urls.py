from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_dojo', views.register_dojo),
    path('create_ninja', views.register_ninja),
    path('delete_dojo_id', views.delete_dojo_id),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_user', views.submit_user),
    path('remove_user_by_id', views.remove_user_by_id),
    path('delete_by_id', views.delete_by_id),
]
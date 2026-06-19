from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.display_all),
    path('shows/new', views.add_show_page),
    path('create_show', views.add_show),
    path('shows/<int:id>', views.show_details),
    path('shows/<int:id>/edit', views.update_page),
    path('edit_show/<int:id>', views.edit_show),
    path('shows/<int:id>/destroy', views.delete_show)
]
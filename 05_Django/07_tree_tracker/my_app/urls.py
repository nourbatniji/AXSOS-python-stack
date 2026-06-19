from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.login),
    path('sign_out/', views.sign_out),
    path('dashboard', views.dashboard),
    path('add_tree_page', views.add_tree_page),
    path('create_tree', views.create_tree),
    path('delete_tree', views.delete_tree),
    path('tree_details_page/<int:id>', views.tree_details_page),
    path('edit_tree_page/<int:id>', views.edit_tree_page),
    path('edit_tree/<int:id>', views.edit_tree),
    path('zipcode_page/<int:id>', views.zipcode_page),
    path('visit_tree/<int:id>', views.visit_tree),
]
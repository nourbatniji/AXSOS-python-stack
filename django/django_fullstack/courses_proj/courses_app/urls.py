from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('courses/destroy/<int:id>', views.delete_course_page),
    path('delete/<int:id>', views.delete_course),
    path('courses/comment/<int:id>', views.comments_page),
    path('add_comment/<int:id>', views.add_comment),
    path('delete_comment/<int:id>', views.delete_comment)
]
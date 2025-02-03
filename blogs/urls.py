from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_blog_controller,get_one_blog_controller,create_blog_controller, manage_blog_controller

router = DefaultRouter()

urlpatterns = [
    path('', get_blog_controller , name='get blogs'),
    path('<int:id>/', get_one_blog_controller , name='get one blog'),
    path("manage/", create_blog_controller , name='create blog'),
    path("manage/<int:id>/", manage_blog_controller , name='update / delete blog'),
]

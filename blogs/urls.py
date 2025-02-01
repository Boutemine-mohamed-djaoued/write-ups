from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import blog_controller,categories_controller

router = DefaultRouter()

urlpatterns = [
    path('', blog_controller , name='blog_controller'),
    path('categories/', categories_controller , name='categories_controller'),

]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import blog_controller,one_blog_controller

router = DefaultRouter()

urlpatterns = [
    path('', blog_controller , name='get/add blogs'),
    path('<int:id>/', one_blog_controller , name='get/delete/update one blog'),
]

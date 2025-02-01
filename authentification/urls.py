from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_controller,status_controller,login_controller

router = DefaultRouter()

urlpatterns = [
    path('register', register_controller , name='register_controller'),
    path('login', login_controller , name='login_controller'),
    path('status', status_controller , name='status-controller'),
]

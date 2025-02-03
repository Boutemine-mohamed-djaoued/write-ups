from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register_controller,login_controller,logout_controller

router = DefaultRouter()

urlpatterns = [
    path('register/', register_controller , name='regester'),
    path('login/', login_controller , name='login'),
    path('logout/',logout_controller, name="logout")
]

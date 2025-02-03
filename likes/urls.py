from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
  path('like/<int:id>/',views.like_unlike_blog,name="like")
]

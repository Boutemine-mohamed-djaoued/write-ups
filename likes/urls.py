from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
 path('like/<int:id>/',views.like_unlike_blog,name="like"),
 path('',views.get_likes,name="get_all_likes"),
 path('user/<int:id>/',views.get_likes_by_user,name="get_likes_by_user"),
 path('blog/<int:id>/',views.get_likes_by_blog,name="get_likes_by_blog"),
]

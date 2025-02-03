from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import categories_controller, delete_category_controller

router = DefaultRouter()

urlpatterns = [
    path('', categories_controller , name='get / add categories'),
    path("<int:id>/", delete_category_controller , name='delete categories'),
]

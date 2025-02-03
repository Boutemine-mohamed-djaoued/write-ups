from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Schema view for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="write-ups API Documentation",
        default_version='v1',
        description="shellmates write-ups API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Allow any user to access the documentation
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentification.urls')),
    path('blogs/', include('blogs.urls')),
    path('categories/', include('categories.urls')),
    path('likes/', include('likes.urls')),
    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
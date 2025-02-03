from django.shortcuts import render
from .models import Like
from blogs.models import Blog
from categories.models import Categories
from blogs.serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from authentification.middleware import authenticated


@api_view(['POST'])
@authenticated
def like_unlike_blog(request, id):
    
    user = request.user

    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({"error": "Blog not found"}, status=404)

    like, created = Like.objects.get_or_create(blog=blog, user=user)

    if not created:
        like.delete()  # Unlike the post
        return Response({"response": "Unliked the blog"}, status=200)

    return Response({"response": "Liked the blog"}, status=201)
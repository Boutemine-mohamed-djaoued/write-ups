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
from .serializers import LikeSerializer
from .docs import like_unlike_docs, get_likes_docs, get_likes_by_user_docs, get_likes_by_blog_docs

@like_unlike_docs
@api_view(['POST'])
@authenticated()
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

@get_likes_docs
@api_view(['GET'])
@authenticated()
def get_likes(request):
    likes=Like.objects.all()
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)

@get_likes_by_user_docs
@api_view(['GET'])
@authenticated()
def get_likes_by_user(request,id):
    """
    gets the likes done by a given user
    """
    likes=Like.objects.filter(user=id)
    if not likes:
        return Response({"error":"the user doesn't exist or has never liked a blog"})
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)

@get_likes_by_blog_docs
@api_view(['GET'])
@authenticated()
def get_likes_by_blog(request,id):
    """
    gets the likes on a given blog
    """
    likes=Like.objects.filter(blog=id)
    if not likes:
        return Response({"error":"the blog doesn't exist or has no likes"})
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)
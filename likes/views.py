from .models import Like
from blogs.models import Blog
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentification.middleware import authenticated
from .serializers import LikeSerializer


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

@api_view(['GET'])
@authenticated
def get_likes(request):
    likes=Like.objects.all()
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)

@api_view(['GET'])
@authenticated
def get_likes_by_user(request,id):
    likes=Like.objects.filter(user=id)
    if not likes:
        return Response({"error":"the user doesn't exist or has never liked a blog"})
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)

@api_view(['GET'])
@authenticated
def get_likes_by_blog(request,id):
    likes=Like.objects.filter(blog=id)
    if not likes:
        return Response({"error":"the blog doesn't exist or has no likes"})
    serializer=LikeSerializer(likes,many=True)
    return Response(serializer.data,status=200)


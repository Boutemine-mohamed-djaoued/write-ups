from .models import Blog
from categories.models import Categories
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from authentification.middleware import authenticated


@api_view(['GET'])
def get_blog_controller(request):
    blogs = Blog.objects.all()
    paginator = PageNumberPagination() #add ?page=i to the url to get the i*th page
    result_page = paginator.paginate_queryset(blogs,request)
    serializer = BlogSerializer(result_page, many=True, context={'request': request})
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_one_blog_controller(request,id):
    blog = get_object_or_404(Blog,id=id)
    if blog:
        serializer = BlogSerializer(blog,context={'request': request})
        return Response(serializer.data, status=200)


@api_view(['POST'])
@authenticated
def create_blog_controller(request):
    if (request.method == 'POST'):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            blog = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@api_view(['DELETE','PUT'])
@authenticated
def manage_blog_controller(request,id):
    if (request.method == 'PUT'):
        blog = get_object_or_404(Blog,id=id)
        if blog :
            serializer = BlogSerializer(blog, data=request.data, partial=True)
            if serializer.is_valid():
                blog = serializer.save()
                return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    if (request.method == 'DELETE'):
        blog = get_object_or_404(Blog,id=id)
        print(id)
        if blog :
            blog.delete()
            return Response(status=204)
        return Response(status=404)

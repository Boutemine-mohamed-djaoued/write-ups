from django.http import JsonResponse
from .models import Blog
from categories.models import Blogs_Categories, Categories
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from authentification.middleware import authenticate_request

@api_view(['GET','POST'])
def blog_controller(request):
    if request.method == 'GET':
        category_id = request.query_params.get('categoryId')  # Filter by category ID
        user_id = request.query_params.get('userId')  # Filter by user ID
        blogs = Blog.objects.all()
        if category_id:
            blogs = blogs.filter(blogs_categories__category_id=category_id)  # Correct filtering
        if user_id:
            blogs = blogs.filter(user_id=user_id)
        paginator = PageNumberPagination()  # Add ?page=i to the URL to get the i-th page
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True, context={'request': request})
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        user_or_error = authenticate_request(request)
        if isinstance(user_or_error, JsonResponse):
            return user_or_error
        data = request.data.copy()
        data['user'] = user_or_error.id
        categories = data.pop('categories', [])
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            blog = serializer.save()
            for category_id in categories:
                try:
                    category = Categories.objects.get(id=category_id)
                    Blogs_Categories.objects.create(category_id=category, blog_id=blog)
                except Categories.DoesNotExist:
                    return Response({"error": f"Category with ID {category_id} does not exist"}, status=400)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','DELETE','PUT'])
def one_blog_controller(request,id):
    if (request.method == 'GET'):
        blog = get_object_or_404(Blog,id=id)
        if blog:
            serializer = BlogSerializer(blog,context={'request': request})
            return Response(serializer.data, status=200)
    user_or_error = authenticate_request(request)
    if isinstance(user_or_error, JsonResponse):
        return user_or_error
    if request.method == 'PUT':
        blog = get_object_or_404(Blog, id=id)
        if blog:
            data = request.data.copy()
            categories = data.pop('categories', None)
            serializer = BlogSerializer(blog, data=data, partial=True)
            if serializer.is_valid():
                blog = serializer.save()
                if categories is not None:
                    Blogs_Categories.objects.filter(blog_id=blog).delete()
                    for category_id in categories:
                        try:
                            category = Categories.objects.get(id=category_id)
                            Blogs_Categories.objects.create(category_id=category, blog_id=blog)
                        except Categories.DoesNotExist:
                            return Response({"error": f"Category with ID {category_id} does not exist"}, status=400)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
    if (request.method == 'DELETE'):
        blog = get_object_or_404(Blog,id=id)
        if blog :
            blog.delete()
            return Response(status=204)
        return Response(status=404)

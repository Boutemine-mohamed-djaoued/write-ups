from authentification.middleware import authenticated
from .models import Blog, Categories
from .serializers import BlogSerializer,CategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


@api_view(['GET','POST','DELETE','PUT'])
# @authenticated
def blog_controller(request):
    if (request.method == 'GET'):
        blog_id = request.GET.get('id')
        print("i am here in GET", blog_id)
        if blog_id:
            print("i am here by ID")
            blog = get_object_or_404(Blog,id=blog_id)
            if blog:
                serializer = BlogSerializer(blog,context={'request': request})
                return Response(serializer.data, status=200)
        blogs = Blog.objects.all()
        paginator = PageNumberPagination() #add ?page=i to the url to get the i*th page
        result_page = paginator.paginate_queryset(blogs,request)
        serializer = BlogSerializer(result_page, many=True, context={'request': request})
        return Response(serializer.data, status=200)
    if (request.method == 'POST'):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            blog = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if (request.method == 'PUT'):
        blog = get_object_or_404(Blog,id=request.data.get('id'))
        if blog :
            serializer = BlogSerializer(blog, data=request.data, partial=True)
            if serializer.is_valid():
                blog = serializer.save()
                return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
      
    if (request.method == 'DELETE'):
      blog = get_object_or_404(Blog,id=request.data.get('id'))
      if blog : 
        blog.delete()
        return Response(status=204)
      return Response(status=404)
      


@api_view(['GET','POST','DELETE'])
@authenticated
def categories_controller(request): 
    if request.method == 'GET':
      categories = Categories.objects.all()
      serializer = CategoriesSerializer(categories, many=True)
      return Response(serializer.data, status=200)
    if request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        category = Categories.objects.get(id=request.data.get('id'))
        if category:
            category.delete()
            return Response(status=204)
        return Response({"error": "ID is required to delete a category"}, status=400)

        
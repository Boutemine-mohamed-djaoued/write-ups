from authentification.middleware import authenticated
from .models import Blog, Categories
from .serializers import BlogSerializer,CategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET','POST','DELETE','PUT'])
@authenticated
def blog_controller(request):
    if (request.method == 'GET'):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=200)
    if (request.method == 'POST'):
        request.data['user'] = request.user.id
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if (request.method == 'PUT'):
      # not implemented yet
      return
    if (request.method == 'DELETE'):
      # not implemented yet
      return


@api_view(['GET','POST','DELETE'])
# @authenticated
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

        
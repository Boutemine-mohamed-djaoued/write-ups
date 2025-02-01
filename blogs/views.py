from authentification.middleware import authenticated
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

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


from django.http import JsonResponse
from categories.models import Categories
from .serializers import CategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentification.middleware import authenticated, authenticate_request
from django.shortcuts import get_object_or_404
from .docs import category_list_docs, category_create_docs, category_delete_docs

@category_list_docs
@category_create_docs
@api_view(['GET','POST'])
def categories_controller(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=200)
    user_or_error = authenticate_request(request)
    if isinstance(user_or_error, JsonResponse):
        return user_or_error
    if (user_or_error.role != 'admin'):
        return Response({"error": "You are not authorized to create a category"}, status=403)
    if request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@category_delete_docs
@api_view(['DELETE'])
@authenticated(role='admin')
def delete_category_controller(request,id):
    print(request.data)
    category = get_object_or_404(Categories,id=id)
    if category:
        category.delete()
        return Response(status=204)
    return Response({"error": "ID is required to delete a category"}, status=400)

from categories.models import Categories
from .serializers import CategoriesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authentification.middleware import authenticated
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
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


@api_view(['DELETE'])
def delete_category_controller(request,id):
    print(request.data)
    category = get_object_or_404(Categories,id=id)
    if category:
        category.delete()
        return Response(status=204)
    return Response({"error": "ID is required to delete a category"}, status=400)
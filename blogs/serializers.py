from rest_framework import serializers
from .models import Blog, Categories

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'content', 'user']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        request = self.context.get('request')
        if request and request.GET.get('id') is None:
            data.pop('content', None)
            
        return data

    def create(self, validated_data):
        blog = Blog.objects.create(**validated_data)
        return blog
    
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

    def create(self, validated_data):
        category = Categories.objects.create(**validated_data)
        return category

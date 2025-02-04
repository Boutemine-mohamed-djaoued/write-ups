from rest_framework import serializers
from likes.models import Like
from .models import Blog
from categories.models import Blogs_Categories

class BlogSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'content', 'user', 'categories' , 'likes_count']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
    def get_categories(self, obj):
        blog_categories = Blogs_Categories.objects.filter(blog_id=obj).select_related('category_id')
        return [blog_category.category_id.name for blog_category in blog_categories]
    def get_likes_count(self, obj):
        return obj.likes.count()
    def create(self, validated_data):
        blog = Blog.objects.create(**validated_data)
        return blog
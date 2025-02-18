from rest_framework import serializers
from categories.models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

    def create(self, validated_data):
        category = Categories.objects.create(**validated_data)
        return category

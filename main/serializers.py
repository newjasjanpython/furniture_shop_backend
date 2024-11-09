from rest_framework.serializers import ( ModelSerializer, ReadOnlyField )
from .models import Category, Product


class ModelStandartReadOnly:
    id = ReadOnlyField(source='pk')
    guid = ReadOnlyField(source='guid')
    created_at = ReadOnlyField(source='created_at')
    updated_at = ReadOnlyField(source='updated_at')


class CategorySerializer(ModelStandartReadOnly, ModelSerializer):
    title = ReadOnlyField()

    class Meta:
        model = Category
        fields = ['id', 'guid', 'title', 'created_at']


class AdminCategorySerializer(ModelStandartReadOnly, ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'guid', 'title', 'created_at', 'updated_at']


class ProductSerializer(ModelStandartReadOnly, ModelSerializer):
    title = ReadOnlyField()
    images = ReadOnlyField(source='get_images')
    description = ReadOnlyField()
    price = ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'guid', 'images', 'title', 'description', 'price', 'created_at', 'updated_at']


class AdminProductSerializer(ModelStandartReadOnly, ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'guid', 'thumbnail', 'title', 'description', 'price', 'created_at', 'updated_at']

from rest_framework import serializers

from magazin.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = 'id title description price category tags reviews'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews']



class ProductActivTagSerializer(serializers.ModelSerializer):
    activ_tag = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'activ_tag']

    def get_activ_tag(self, product):
        tags = Tag.objects.filter(product=product).exclude(is_active=False)
        return  TagSerializer(tags, many=True).data
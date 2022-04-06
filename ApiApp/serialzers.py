from rest_framework import serializers
from ApiApp.models import ProductModel

class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

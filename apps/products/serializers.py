from .models import Item
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)
    
    
    class Meta:
        model = Item
        fields = '__all__'
from rest_framework import generics
from .serializers import ItemSerializer
from django.http import JsonResponse
from .models import Item


class ItemList(generics.ListAPIView):
     queryset = Item.objects.order_by('created_at')
     
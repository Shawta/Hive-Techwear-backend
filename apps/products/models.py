from django.db import models
from cloudinary.models import CloudinaryField
from config.constants import STATUS,ITEM_TYPE
from apps.categories.models import Category



class Item(models.Model):
    class Meta(object):
        db_table = 'item'
        
   
    name = models.CharField(
        'Name', blank=False, null=False, max_length=50,  
    )
    
    description = models.CharField(
        'Description', blank=True, null=True, max_length=255
    )
    
    price = models.FloatField(
        'Price', blank=False, null=False
        
    )
    
    type = models.CharField(
        'Type', blank=False, null=False, max_length=50, choices=ITEM_TYPE
    )
    
    image = CloudinaryField(
        'Item Image', blank=True, null=True
    )
    
    category = models.ForeignKey(
        Category, related_name='related_category', on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
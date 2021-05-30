from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=20,blank=True)
    description = models.TextField(blank=True)
    price= models.IntegerField()
    bedrooms = models.IntegerField(blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1,blank=True)
    garage = models.IntegerField(default=0,blank=True)
    sqft = models.IntegerField(blank=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y%m%d/',blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank = True)

    def __str__(self):
        return self.title
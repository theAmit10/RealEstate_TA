from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    relator = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # here if we delete something from thre relator which is the foriegn key we are declearing what to do during deleting something in foreign key.
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # now this is optional duw to blank.
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # i.e 2.9
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/' )
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True) # now this all 6 field are optional.
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self): # selecting the main fiels to be displayed.
        return self.title


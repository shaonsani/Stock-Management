from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Owner(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=50, blank=True, null=True)
   email = models.CharField(max_length=50)

   def __str__(self):
       return self.name

class Product(models.Model):
    name =  models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='product_pics')

    def __str__(self):
        return self.name +' '+str(self.price)
    
    def get_absolute_url(self):
        return reverse('APP:store')
        

class History(models.Model):
    name =  models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField()
    createdTime=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
           return f'{self.desc} {self.price} '
    
# Create your models here.
class Order(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField()
    createdTime=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
           return f'{self.desc}  '
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    def __str__(self):
        return 
    
class Productsall(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    def __str__(self):
        return 
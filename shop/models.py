from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=400)
    pub_date = models.DateField()
    image = models.ImageField()
    

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25) 
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
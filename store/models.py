from django.db import models

from django.contrib.auth.models import User

# 
# class ProductCatagory(models.Model):
#     catagoryName=models.CharField(max_length=200,null=False,blank=False)

#     def __str__(self):
#         return self.catagoryName


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    # description= models.TextField(max_length=500,null=True,blank=True)
    # catagory=models.CharField(max_length=200)
    price = models.FloatField(default=0)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image=models.ImageField(upload_to='%d',default='default.jpg')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    # date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        
        return self.transaction_id


class ShippingAddress(models.Model):
    customer = models.ForeignKey( Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

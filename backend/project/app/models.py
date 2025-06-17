from django.db import models
from django.utils import timezone

class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    number = models.BigIntegerField()
    email = models.EmailField()
    productName = models.CharField(max_length=255)
    productPrice = models.CharField(max_length=50)
    productImage = models.TextField()
    quantity = models.IntegerField(default=1)
    totalAmount = models.FloatField()
    razorpay_payment_id = models.CharField(max_length=255)
    razorpay_signature = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    razorpay_order_id = models.CharField(max_length=255, default='', blank=True)
    payment_mode = models.CharField(max_length=50, default='COD')  # or 'online' or whatever you use
    
    def __str__(self):
        return f"{self.name} - {self.productName}"

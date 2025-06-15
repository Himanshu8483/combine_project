from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.BigIntegerField()
    payment = models.CharField(max_length=50)

    email = models.EmailField()
    productName = models.CharField(max_length=100)
    # productImage = models.URLField(max_length=300)
    productImage = models.CharField(max_length=200)

    quantity = models.IntegerField(default=1)
    productPrice = models.FloatField()
    totalAmount = models.FloatField()
    def __str__(self):
        return f"{self.name} - {self.productName}"

from rest_framework import serializers
from .models import *
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        # fields = ['id', 'name', 'address', 'number', 'payment']
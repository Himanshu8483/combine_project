from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
    
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({
            "amount": int(data['amount']) * 100,  # convert to paise
            "currency": "INR",
            "payment_capture": "1"
        })
        return JsonResponse(payment)


import hmac
import hashlib
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

@csrf_exempt
def verify_payment(request):
    import json
    data = json.loads(request.body)

    order_id = data.get('razorpay_order_id')
    payment_id = data.get('razorpay_payment_id')
    signature = data.get('razorpay_signature')

    msg = f"{order_id}|{payment_id}"
    generated_signature = hmac.new(
        settings.RAZORPAY_KEY_SECRET.encode(),
        msg.encode(),
        hashlib.sha256
    ).hexdigest()

    if generated_signature == signature:
        # ✅ Save order to database
        # Order.objects.create(...your data...)
        return JsonResponse({"status": "Payment verified"})
    else:
        return HttpResponseBadRequest("Payment verification failed")


from django.http import FileResponse
import os

def index(request):
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'dist', 'index.html')
    return FileResponse(open(file_path, 'rb'))

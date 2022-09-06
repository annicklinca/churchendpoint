from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import HttpResponse, JsonResponse
import requests
from .serializers import *
import hashlib
import random

# Create your views here.

@csrf_exempt
def home(request):
    return HttpResponse('<center><font color="steelblue"><h1>Welcome to Bchurch</h1></font></center>')

####..create account  

@csrf_exempt
def Charity(request):


   
    data={
        'username':'bob',
        'timestamp':'20161231115242',
        'amount':100,
        'password': 'd3cfd05492a2376003f5af9e2e6643b67',
        'mobilephone': 250785971082,
        'requesttransactionid':34555
        }
    response=requests.post('https://www.intouchpay.co.rw/api/requestpayment/', data=data)

@csrf_exempt
def ChurchDonation(request):
   
    if request.method == 'GET':
        reg = Church.objects.all()
        serializer = ChurchSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        if str(data['paymentway'])=='MTN Mobile Money':
            username='testa'
            partnerpassword='pass123456789'
            accountid='250160000011'
            timestamp='20221231115242'
            password=hashlib.sha256((str(username)+(accountid)+partnerpassword+timestamp).encode('utf-8')).hexdigest()
            databody={
            'username':username,
            'timestamp':timestamp,
            'amount':data['amount'],
            'password': password,
            'mobilephone': data['phone'],
            'requesttransactionid':random.randint(100, 98887675675565)
            }
            response=requests.post('https://www.intouchpay.co.rw/api/requestpayment/', data=databody).json()
            serializer = ChurchSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'successful','response':response}, status=201)
            return JsonResponse(serializer.errors, status=400)
        serializer = ChurchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful','response':'Success'}, status=201)
        return JsonResponse(serializer.errors, status=400)
        
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.

@csrf_exempt
def home(request):
    return HttpResponse('<center><font color="steelblue"><h1>Welcome to tourism</h1></font></center>')

####..create account  

@csrf_exempt
def Charity(request):
   
    if request.method == 'GET':
        reg = Charity.objects.all()
        serializer = CharitySerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = CharitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  

@csrf_exempt
def ChurchDonation(request):
   
    if request.method == 'GET':
        reg = Church.objects.all()
        serializer = ChurchSerializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request.data
        serializer = ChurchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful'}, status=201)
        return JsonResponse(serializer.errors, status=400)  
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import requests
from datetime import date
from api.ML import detection
from .models import Data
from django.core import serializers

# Create your views here.

def Live(request):
    today = date.today()
    x,y = detection.live_cam()
    mod = Data()
    mod.date = today
    mod.drowsy = x
    mod.total = y
    mod.save()
    data = {
        'date': today,
        'drowsy': x,
        'total': y
    }
    return JsonResponse(data)

def Allstats(request):
    queryset = Data.objects.all()
    serialized_queryset = serializers.serialize('python', queryset)
    return JsonResponse(serialized_queryset, safe=False)

def Dailystats(request):
    today = date.today()
    queryset = Data.objects.filter(date = today)
    serialized_queryset = serializers.serialize('python', queryset)
    return JsonResponse(serialized_queryset, safe=False)


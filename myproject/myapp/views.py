from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def index(request):
      return render(request,'index.html',{})

def login(request):
    return render(request,'login.html',{})

def stateitems(request):
    data=state.objects.all()
    Itemobj=student.objects.all()
    return render(request,'state.html',{'state': data})

def testApi(request):
    response = {}
    response = serializers.serialize("json", state.objects.all())
    return HttpResponse(response, content_type="application/json")

def getSubject(request):
    state = request.GET.get('state')
    response = {}
    response = serializers.serialize("json", student.objects.filter(state = state).all())
    return HttpResponse(response, content_type="application/json")

def getAll(request):
    response1 = {}
    response1 = serializers.serialize("json", student.objects.all())
    return HttpResponse(response1, content_type="application/json")
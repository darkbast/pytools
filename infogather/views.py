from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    test_val = 'my test val'
    return render(request,'intogather/test.html',{'message':test_val})

def gather_main(request):
    return HttpResponse("Hello, World! gather_main")

def gather_ins(request):
    return HttpResponse("Hello, World! gather_ins")
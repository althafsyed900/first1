from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def food(request):
    return render(request,'food.html')

def nonveg(request):
    return HttpResponse('<h1>this is non-vegetarians world</h1>')
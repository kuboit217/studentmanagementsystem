from django.shortcuts import render

# Create your views here.

def ShowDemo(request):
    return render(request,'demo.html')
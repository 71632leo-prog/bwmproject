from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 

def autos(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'autos/autos.html') 
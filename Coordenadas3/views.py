from django.shortcuts import render

def homepage (request):
    return render(request,'homepage.html',{})

def coordenada (request):
    return render(request,'coordenada/home.html',{})

def coordenada_mx (request):
    return render(request,'coordenada/coordenada.html',{})
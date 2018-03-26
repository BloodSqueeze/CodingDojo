from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('placeholder to later display a list of blogs')

def new(request):
    return HttpResponse('placeholder to later create new blogs')

def create(request):
    return redirect('/')

def show(request, number):
    response = 'placeholder to later display blog ' + number
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to later edit blog # ' + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/')
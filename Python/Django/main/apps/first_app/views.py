from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    response = 'first app works!'
    return HttpResponse(response)
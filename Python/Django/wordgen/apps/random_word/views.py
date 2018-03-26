from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] = request.session['count'] + 1
    context = {
        'count' : request.session['count'],
        'random' : get_random_string(length=10)
    }
    return render(request, 'random_word/index.html', context)

def process(request):
    return redirect('/')

def delete(request):
    request.session.clear()
    return redirect('/')
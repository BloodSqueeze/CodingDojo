# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render,HttpResponse, redirect
from models import *
import re, bcrypt
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'login/index.html', context)

def register(request):
    valid = True
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    confirm = request.POST['pass_confirm']
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if request.method == 'POST':
        if len(first_name) < 2:
            valid = False
            messages.error(request, 'First Name needs to be longer than 2 Characters')
        if len(last_name) < 2:
            valid = False
            messages.error(request, 'Last Name needs to be longer than 2 Characters')
        if len(email) < 6:
            valid = False
            messages.error(request, 'Email is required and must be in valid format ex: name@email.com')
        if password != confirm:
            valid = False
            messages.error(request, 'Password does not match!')
        if valid == True:
            try:
                User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_password)
                user = User.objects.get(email=email)
                request.session['current_user'] = user.id
                print 'user.id---------------------'
                messages.success(request, 'You have registered successfully and are now logged in')
                return redirect('/logged')
            except Exception as problem:
                print problem
                messages.error(request, 'Email already exists')
    return redirect('/')
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if request.method == 'POST':
        if len(password) > 0:
            try:
                user = User.objects.get(email=email)
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    request.session['current_user'] = user.id
                    print 'user.id---------------------'
                    messages.success(request, 'You have successfully logged in')
                    return redirect('/logged')
                else:
                    messages.error(request, 'you need to remember your password')
                    return redirect('/')
            except Exception as problem:
                messages.error(request, 'you need to register first')
                print problem
                return redirect('/')
        else:
            messages.error(request, 'you need to submit a password to continue')
            return redirect('/')
    return redirect('/login)')

def logged(request):
    if 'current_user' in request.session:
        context = {
            'user': User.objects.get(id=request.session['current_user'])
        }
    return redirect('/courses')

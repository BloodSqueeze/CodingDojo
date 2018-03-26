from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new_user.html')

def create(request):
    user_first = request.POST['first_name']
    user_last = request.POST['last_name']
    email = request.POST['email']
    User.objects.create(first_name=user_first, last_name=user_last, email=email)
    return redirect('/')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    print user_id
    return render(request, 'users/show.html', context)

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
    }
    return render(request, 'users/edit_form.html', context)

def update(request, user_id):
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    print user.first_name
    return redirect('/')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    print "deleting" + user_id
    return redirect('/')
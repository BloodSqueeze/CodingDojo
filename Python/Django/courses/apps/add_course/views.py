from django.shortcuts import render, HttpResponse, redirect
from ..login.models import User
# Create your views here.
def index(request):
    if 'current_user' in request.session:
        context = {
            'user': User.objects.get(id=request.session['current_user'])
        }
    return render(request, 'add_course/courses.html', context)

def create(request):
    
    return redirect('/courses/')
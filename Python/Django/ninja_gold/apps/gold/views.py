from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random
from random import *
import string
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = int(0)
    if 'log' not in request.session:
        request.session['log'] = []
    if 'name' not in request.session:
        request.session['name'] = []
    context = {
        'count': request.session['count'],
        'logs': request.session['log'],
        'player': request.session['name'],
    }
    return render(request, 'gold/index.html', context)

def process_money(request):
    if request.method == 'POST':
        activity = request.POST['html_activity']
        if activity == 'farm':
            print 'so far so good **********'
            gold = randint(10,20)
            print gold
            request.session['count'] = int(request.session['count']) + int(gold)
            request.session['log'].insert(0, 'you have added ' + str(gold) + ' gold at the farm')
        if activity == 'cave':
            print 'so far so good **********'
            gold = randint(5,10)
            print gold
            request.session['count'] = int(request.session['count']) + int(gold)
            request.session['log'].insert(0, 'you have added ' + str(gold) + ' gold at the cave')
        if activity == 'house':
            print 'so far so good **********'
            gold = randint(2,5)
            print gold
            request.session['count'] = int(request.session['count']) + int(gold)
            request.session['log'].insert(0, 'you have added ' + str(gold) + ' gold at the house')
        if activity == 'casino':
            print 'so far so good **********'
            gold = randint(-50,50)
            print gold
            request.session['count'] = int(request.session['count']) + int(gold)
            if gold > 0:
                request.session['log'].insert(0, 'you have added ' + str(gold) + ' gold at the casino')
            else:
                gold = gold * -1
                request.session['log'].insert(0, 'you have lost ' + str(gold) + ' gold at the casino')
    return redirect('/')

def name(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['player']
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

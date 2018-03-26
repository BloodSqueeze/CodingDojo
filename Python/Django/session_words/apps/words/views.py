from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
        
    context = {
        'dictionary': request.session['words']
    }
    print request.session['words']
    return render(request, 'words/index.html', context)

def process(request):
    if request.method == 'POST':
        word = {
        'content': request.POST['word'],
        'color': request.POST['color'],
        'size': request.POST['size'],
        }
        request.session['words'].append(word)
    print word
    print 'next is words ---------->>>>>>>>>>'
    print request.session['words']
    
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')


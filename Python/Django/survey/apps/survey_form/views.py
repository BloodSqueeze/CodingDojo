from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print '---------->>>>><<<<<<-----'
    if 'name' not in request.session:
        request.session['name'] = []
    if 'location' not in request.session:
        request.session['location'] = []
    if 'language' not in request.session:
        request.session['language'] = []
    if 'comment' not in request.session:
        request.session['comment'] = []
    print 'session now active -*********'
    return render(request, 'survey_form/index.html')

def process(request):
    print 'It worked perfectly------>>>>'
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if 'count' not in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] = request.session['count'] + 1
    return redirect('/result')

def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count'],
        }
    
    return render(request, 'survey_form/result.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')
from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    return render(request,"word_app/index.html")


def generate(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count']+=1
    
    request.session['word'] = get_random_string(length=14)

    return redirect('/')

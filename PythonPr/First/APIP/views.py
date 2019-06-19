from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def index (request):
    return render_to_response('index.html')
def string(request):
    return HttpResponse('Hello. Api is coming!')
# Create your views here.

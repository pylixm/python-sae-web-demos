# -*- coding: utf-8 -*-
# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

def index(request):
    try:
        dt = datetime.datetime.now() 
        context = {}
        context['dt'] = dt
        return render_to_response('index.html',context )
    except ValueError:
        raise Http404()

def test(request, idx):
    return render_to_response('bs/test%s.html'%idx )
    
def markdown(request):
    try:
        dt = datetime.datetime.now() 
        context = {}
        context['dt'] = dt
        return render_to_response('markdown.html',context )
    except ValueError:
        raise Http404()
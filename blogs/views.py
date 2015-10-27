from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect,HttpResponse,render_to_response
import django

def home(req):
    return render_to_response("index.html")


def test(req):
    return HttpResponse("<p>The Django is version %s</p>"%django.get_version())
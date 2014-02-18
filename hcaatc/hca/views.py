from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from django import http
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def about1(request):
    return render_to_response('about_1.html')

def contact(request):
    return render_to_response('contact.html')

def course(request):
    return render_to_response('course.html')

@login_required
def c(request):
    return render_to_response('c.html')

@login_required
def fee(request):
    return render_to_response('fee.html')


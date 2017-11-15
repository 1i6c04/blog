from django.shortcuts import render
from django.core.paginator import Page
import datetime


def main(request):
    '''
    Render the main page
    '''
    now = datetime.datetime.now()
    context = {'like':'Django 很棒','now':now}
    return render(request, 'main/main.html', context)
def about(request):
    '''
    rander the about Page
    '''
    return render(request,'main/about.html')
    
# Create your views here.

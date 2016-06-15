from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def view_years(request):
    title = 'Hello World'
    template = loader.get_template('viewyears.html')
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

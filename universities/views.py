from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import University
from .forms import UniversityForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/')
def new_university(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            year = form.save()
            year.save()
            return HttpResponseRedirect('/')
    else:
        form = UniversityForm()

    title = 'Sistema de Evaluacion Institucional'
    template = loader.get_template('new_university.html')
    context = {
        'title': title,
        'form': form
    }
    return HttpResponse(template.render(context, request))
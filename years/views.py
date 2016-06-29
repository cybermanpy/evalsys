from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Year
from .forms import YearForm

# Create your views here.

def view_years(request):
    title = 'Sistema de Evaluacion Institucional'
    year = Year.objects.all()
    template = loader.get_template('year_view.html')
    context = {
        'title': title,
        'year': year
    }
    return HttpResponse(template.render(context, request))

def year_detail(request, pk):
    title = 'Sistema de Evaluacion Institucional'
    year = get_object_or_404(Year, pk=pk)
    template = loader.get_template('year_detail.html')
    context = {
        'title': title,
        'year': year
    }
    return HttpResponse(template.render(context, request))


def new_year(request):
    if request.method == 'POST':
        form = YearForm(request.POST)
        #form = YearForm(request.POST, request.FILES)
        if form.is_valid():
            year = form.save()
            year.save()
            return HttpResponseRedirect('/')
    else:
        form = YearForm()

    title = 'Sistema de Evaluacion Institucional'
    template = loader.get_template('new_year.html')
    context = {
        'title': title,
        'form': form
    }
    return HttpResponse(template.render(context, request))

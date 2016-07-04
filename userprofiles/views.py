from django.shortcuts import redirect, render_to_response
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
# Create your views here.

def authentication(request):
    title = 'Sistema de Evaluacion Institucional'
    template = loader.get_template('login.html')
    context = {
        'title': title,
    }
    if not request.user.is_anonymous():
        return redirect('/dashboard')
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        contextno = {
            'error': True,
            'username': username,
            'title': title
        }
        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
        elif action == 'login':
            access = authenticate(username=username, password=password)
            if access is not None:
                if access.is_active:
                    login (request, access)
                    return redirect('/dashboard')
                else:
                    templateNoActive = loader.get_template('noactive.html')
                    return HttpResponse(templateNoActive.render(contextno, request))
            else:
                templateNoUser = loader.get_template('nouser.html')
                return HttpResponse(templateNoUser.render(contextno, request))
    return HttpResponse(template.render(context, request))

@login_required(login_url='/')
def home(request):
    title = 'Sistema de Evaluacion Institucional'
    template = loader.get_template('home.html')
    context = {
        'title': title,
    }
    return HttpResponse(template.render(context, request))

# def authentication(request):
#     title = 'Sistema de Evaluacion Institucional'
#     template = loader.get_template('login.html')
#     context = {
#         'title': title,
#     }
#     if not request.user.is_anonymous():
#         return redirect('/dashboard')
#     if request.method == 'POST':
#         action = request.POST.get('action', None)
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if action == 'signup':
#             user = User.objects.create_user(username=username, password=password)
#             user.save()
#         elif action == 'login':
#             user = authenticate(username=username, password=password)
#             login(request, user)
#         return redirect('/dashboard')
#     return HttpResponse(template.render(context, request))
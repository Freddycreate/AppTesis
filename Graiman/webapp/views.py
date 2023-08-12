from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

from molienda.models import Atomizado, Barbotina, Granulometria


# Create your views here.
@login_required
def bienvenido(request):
    usuario = request.user
    nombre_groups = [g.name for g in usuario.groups.all()]
    if "administradores" in nombre_groups:
        no_silos = Atomizado.objects.count()
        silos = Atomizado.objects.order_by('-id')[0:100]
    else:
        silos = Atomizado.objects.filter(usuario=request.user).order_by('-id')
        no_silos = Atomizado.objects.filter(usuario=request.user).count()
    return render(request, 'bienvenido.html', {'no_silos_registrados': no_silos, 'Silos': silos})



def barbotina(request):
    usuario = request.user
    nombre_groups = [g.name for g in usuario.groups.all()]
    if "administradores" in nombre_groups:
        no_bar = Barbotina.objects.count()
        bar = Barbotina.objects.order_by('-id')[0:100]
    else:
        bar = Barbotina.objects.filter(usuario=request.user).order_by('-id')
        no_bar = Barbotina.objects.filter(usuario=request.user).count()
    return render(request, 'barbotina.html', {'no_bar_registrados': no_bar, 'Bar': bar})



def granulometria(request):
    usuario = request.user
    nombre_groups = [g.name for g in usuario.groups.all()]
    if "administradores" in nombre_groups:
        no_granu = Granulometria.objects.count()
        granu = Granulometria.objects.order_by('-id')[0:100]
    else:
        granu = Granulometria.objects.filter(usuario=request.user).order_by('-id')
        no_granu = Barbotina.objects.filter(usuario=request.user).count()
    return render(request, 'granulometria.html', {'no_granu_registrados': no_granu, 'Granu': granu})













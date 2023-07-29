from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template

from molienda.models import Atomizado, Barbotina, Granulometria


# Create your views here.
@login_required
def bienvenido(request):
    no_silos = Atomizado.objects.count()
    silos = Atomizado.objects.order_by('-id')
    return render(request, 'bienvenido.html', {'no_silos_registrados': no_silos, 'Silos': silos})


def barbotina(request):
    no_bar = Barbotina.objects.count()
    bar = Barbotina.objects.order_by('-id')
    return render(request, 'barbotina.html', {'no_bar_registrados': no_bar, 'Bar': bar})


def granulometria(request):
    no_granu = Granulometria.objects.count()
    granu = Granulometria.objects.order_by('-id')
    return render(request, 'granulometria.html', {'no_granu_registrados': no_granu, 'Granu': granu})














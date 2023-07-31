from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from Graiman.forms import AtomizadoForm, BarbotinaForm, GranulometriaForm
from molienda.models import Atomizado, Barbotina, Granulometria
from django.utils import timezone

# Create your views here.

def salir(request):
    logout(request)
    return redirect("/")


def detalleAtomizado(request, id):
    #    silos = Atomizado.objects.get(pk=id)
    # tambien se lo podria codificar para que salga como pag no encontrada 404
    silos = get_object_or_404(Atomizado, pk=id)
    return render(request, 'silos/detalle.html', {'silos': silos})


# AtomizadoForm = modelform_factory(Atomizado, exclude=[])


def nuevoRegistro(request):
    if request.method == 'POST':
        formaSilo = AtomizadoForm(request.POST)
        if formaSilo.is_valid():
            formaSilo.save()
            return redirect('inicio')
    else:
        formaSilo = AtomizadoForm()
        return render(request, 'silos/nuevo.html', {'formaSilo': formaSilo})


def editarRegistro(request, id):
    if request.method == 'POST':
        formaSilo = AtomizadoForm(request.POST)
        if formaSilo.is_valid():
            formaSilo.save()
            return redirect('inicio')

    else:
        silos = get_object_or_404(Atomizado, pk=id)
        formaSilo = AtomizadoForm(instance=silos)
        return render(request, 'silos/editar.html', {'formaSilo': formaSilo})


def eliminarRegistro(request, id):
    silos = get_object_or_404(Atomizado, pk=id)
    if silos:
        silos.delete()
    return redirect('inicio')


 #Barbotinas

def detailBarbotina(request, id):
    bar = get_object_or_404(Barbotina, pk=id)
    return render(request, 'barbotinas/detail.html', {'bar': bar})



def crearRegistro(request):
    if request.method == 'POST':
        formaBar = BarbotinaForm(request.POST)
        if formaBar.is_valid():
            formaBar.save()
            return redirect('barbotina.html')

    else:
        formaBar = BarbotinaForm()
        return render(request, 'barbotinas/crear.html', {'formaBar': formaBar})


def editRegistro(request, id):
    if request.method == 'POST':
        formaBar = BarbotinaForm(request.POST)
        if formaBar.is_valid():
            formaBar.save()
            return redirect('index')

    else:
        bar = get_object_or_404(Barbotina, pk=id)
        formaBar = BarbotinaForm(instance=bar)
        return render(request, 'barbotinas/edit.html', {'formaBar': formaBar})


def deleteRegistro(request, id):
    bar = get_object_or_404(Barbotina, pk=id)
    if bar:
        bar.delete()
    return redirect('index')

# Granulometrias


def verGranulometria(request, id):
    granu = get_object_or_404(Granulometria, pk=id)
    return render(request, 'granulometrias/ver.html', {'granu': granu})



def newRegistro(request):
    if request.method == 'POST':
        formaGranu = GranulometriaForm(request.POST)
        if formaGranu.is_valid():
            formaGranu.save()
            return redirect('ini')

    else:
        formaGranu = GranulometriaForm()
        return render(request, 'granulometrias/new.html', {'formaGranu': formaGranu})


def modificarRegistro(request, id):
    if request.method == 'POST':
        formaGranu = GranulometriaForm(request.POST)
        if formaGranu.is_valid():
            formaGranu.save()
            return redirect('ini')

    else:
        granu = get_object_or_404(Granulometria, pk=id)
        formaGranu = GranulometriaForm(instance=granu)
        return render(request, 'granulometrias/modificar.html', {'formaGranu': formaGranu})


def borrarRegistro(request, id):
    granu = get_object_or_404(Granulometria, pk=id)
    if granu: granu.delete()
    return redirect('ini')










def grafAtomizado(request, start_date=None, end_date=None):
    atomizado = Atomizado.objects.all()

    if start_date:
        atomizado = atomizado.filter(fecha__gte=start_date)
    if end_date:
        atomizado = atomizado.filter(fecha__lte=end_date)

    labels = [dato.fecha.strftime('%Y-%m-%d') for dato in atomizado]
    humedades = [dato.humedad for dato in atomizado]
    nro_silos = [dato.nroSilo for dato in atomizado]
    datos_grafico = {'labels': labels, 'humedades': humedades, 'nro_silos': nro_silos}
    return render(request, 'grafico.html', {'datos_grafico': datos_grafico})


def grafBarbotina(request, start_date=None, end_date=None):
    barbotina = Barbotina.objects.all()

    if start_date:
        barbotina = barbotina.filter(fecha__gte=start_date)
    if end_date:
        barbotina = barbotina.filter(fecha__lte=end_date)

    labels = [dato.fecha.strftime('%Y-%m-%d') for dato in barbotina]
    densidades = [float(dato.densidad) for dato in barbotina]
    viscosidades = [dato.viscosidad for dato in barbotina]
    residuos = [float(dato.residuo) for dato in barbotina]
    datos_grafico = {'labels': labels, 'densidades': densidades, 'viscosidades': viscosidades, 'residuos': residuos}
    return render(request, 'graficobar.html', {'datos_grafico': datos_grafico})








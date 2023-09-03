from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from Graiman.forms import AtomizadoForm, BarbotinaForm, GranulometriaForm, FiltroAtomizadoForm, FiltroBarbotinaForm
from molienda.models import Atomizado, Barbotina, Granulometria
from django.contrib import messages
from django.utils import timezone

# Create your views here.
def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'registration/login.html', informacion_template)

def logout_view(request):
    logout(request)
    messages.info(request, "Vuelve pronto")
    return redirect('inicio')


def salir(request):
    logout(request)
    return redirect("/")


def detalleAtomizado(request, id):
    silos = get_object_or_404(Atomizado, pk=id)
    return render(request, 'silos/detalle.html', {'silos': silos})


def nuevoRegistro(request):
    if request.method == 'POST':
        formaSilo = AtomizadoForm(request.POST)
        print(request.POST)
        print(formaSilo.errors)
        if formaSilo.is_valid():
            registro = formaSilo.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('inicio')
    else:
        formaSilo = AtomizadoForm()
    return render(request, 'silos/nuevo.html', {'formaSilo': formaSilo})


def editarRegistro(request, id):
    silos = get_object_or_404(Atomizado, pk=id)
    if request.method == 'POST':
        formaSilo = AtomizadoForm(request.POST)
        if formaSilo.is_valid():
            silos.delete()
            registro = formaSilo.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('inicio')
    else:
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
            registro = formaBar.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('index')
    else:
        formaBar = BarbotinaForm()
        return render(request, 'barbotinas/crear.html', {'formaBar': formaBar})


def editRegistro(request, id):
    bar = get_object_or_404(Barbotina, pk=id)
    if request.method == 'POST':
        formaBar = BarbotinaForm(request.POST)
        if formaBar.is_valid():
            bar.delete()
            registro = formaBar.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('index')
    else:
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
            registro = formaGranu.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('ini')

    else:
        formaGranu = GranulometriaForm()
        return render(request, 'granulometrias/new.html', {'formaGranu': formaGranu})


def modificarRegistro(request, id):
    granu = get_object_or_404(Granulometria, pk=id)
    if request.method == 'POST':
        formaGranu = GranulometriaForm(request.POST)
        if formaGranu.is_valid():
            granu.delete()
            registro = formaGranu.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('ini')
    else:
        formaGranu = GranulometriaForm(instance=granu)
    return render(request, 'granulometrias/modificar.html', {'formaGranu': formaGranu})


def borrarRegistro(request, id):
    granu = get_object_or_404(Granulometria, pk=id)
    if granu: granu.delete()
    return redirect('ini')


from django.shortcuts import render
from .models import Atomizado


def grafAtomizado(request):
    # Verifica si el usuario actual pertenece al grupo de administradores
    if request.user.groups.filter(name='administradores').exists():
        # El usuario es un administrador, por lo tanto, puede ver todos los datos
        atomizado = Atomizado.objects.all()
    else:
        # El usuario no es un administrador, por lo tanto, solo puede ver sus propios datos
        atomizado = Atomizado.objects.filter(usuario=request.user)

    form = FiltroAtomizadoForm(request.GET)

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        planta = form.cleaned_data.get('planta')

        # Verifica si al menos una de las fechas se proporcionó
        if start_date or end_date:
            # Se proporcionaron fechas, aplicar los filtros
            if start_date:
                atomizado = atomizado.filter(fecha__gte=start_date)
            if end_date:
                atomizado = atomizado.filter(fecha__lte=end_date)

            # Verifica si se proporcionó una planta y aplica el filtro
            if planta:
                atomizado = atomizado.filter(planta__id=planta)
        else:
            # No se proporcionaron fechas, no realizar la consulta
            atomizado = Atomizado.objects.none()

    labels = [dato.fecha.strftime('%Y-%m-%d') for dato in atomizado]
    humedades = [dato.humedad for dato in atomizado]
    nro_silos = [dato.nroSilo for dato in atomizado]
    datos_grafico = {'labels': labels, 'humedades': humedades, 'nro_silos': nro_silos}

    # Devuelve el mensaje si no hay datos
    no_data_message = "No hay datos que mostrar." if not atomizado.exists() else None

    return render(request, 'grafico.html',{'datos_grafico': datos_grafico, 'form': form, 'no_data_message': no_data_message})


def grafBarbotina(request):
    # Verifica si el usuario actual pertenece al grupo de administradores
    if request.user.groups.filter(name='administradores').exists():
        # El usuario es un administrador, por lo tanto, puede ver todos los datos
        barbotina = Barbotina.objects.all()
    else:
        # El usuario no es un administrador, por lo tanto, solo puede ver sus propios datos
        barbotina = Barbotina.objects.filter(usuario=request.user)

    form = FiltroBarbotinaForm(request.GET)

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        planta = form.cleaned_data.get('planta')

        # Verifica si al menos una de las fechas se proporcionó
        if start_date or end_date:
            # Se proporcionaron fechas, aplicar los filtros
            if start_date:
                barbotina = barbotina.filter(fecha__gte=start_date)
            if end_date:
                barbotina = barbotina.filter(fecha__lte=end_date)

            # Verifica si se proporcionó una planta y aplica el filtro
            if planta:
                barbotina = barbotina.filter(planta__id=planta)
        else:
            # No se proporcionaron fechas, no realizar la consulta
            barbotina = Barbotina.objects.none()

    labels = [dato.fecha.strftime('%Y-%m-%d') for dato in barbotina]
    densidades = [float(dato.densidad) for dato in barbotina]
    viscosidades = [dato.viscosidad for dato in barbotina]
    residuos = [float(dato.residuo) for dato in barbotina]
    datos_grafico = {'labels': labels, 'densidades': densidades, 'viscosidades': viscosidades, 'residuos': residuos}

    # Devuelve el mensaje si no hay datos
    no_data_message = "No hay datos que mostrar." if not barbotina.exists() else None

    return render(request, 'graficobar.html',{'datos_grafico': datos_grafico, 'form': form, 'no_data_message': no_data_message})




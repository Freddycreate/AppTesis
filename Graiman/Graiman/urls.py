"""Graiman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from molienda import views
from molienda.views import detalleAtomizado, nuevoRegistro, editarRegistro, eliminarRegistro, crearRegistro, \
    detailBarbotina, \
    editRegistro, deleteRegistro, verGranulometria, modificarRegistro, borrarRegistro, newRegistro, grafAtomizado, \
    grafBarbotina
from webapp.views import bienvenido, barbotina, granulometria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name="salir"),
    path('', bienvenido, name='inicio'),
    path('detalle_registro/<int:id>', detalleAtomizado),
    path('nuevo_registro', nuevoRegistro),
    path('editar_registro/<int:id>', editarRegistro),
    path('eliminar_registro/<int:id>', eliminarRegistro),
    path('barbotina.html', barbotina, name='index'),
    path('crear_registro', crearRegistro),
    path('detail_registro/<int:id>', detailBarbotina),
    path('edit_registro/<int:id>', editRegistro),
    path('delete_registro/<int:id>', deleteRegistro),
    path('granulometria.html', granulometria, name='ini'),
    path('new_registro', newRegistro),
    path('ver_registro/<int:id>', verGranulometria),
    path('modificar_registro/<int:id>', modificarRegistro),
    path('borrar_registro/<int:id>', borrarRegistro),
    path('grafico1/', grafAtomizado, name='grafico1'),
    path('grafico2/', grafBarbotina, name='grafico2'),



]




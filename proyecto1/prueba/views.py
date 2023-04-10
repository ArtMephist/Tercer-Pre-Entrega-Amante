from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, BusquedaForm, RecipeForm, SearchForm
from .models import Datos_Empleados, N_Empleados_P, N_Emp_Total

# Create your views here.


def respuesta(request):
    Empleados = Datos_Empleados.objects.all()
    Datos_puestos = N_Empleados_P.objects.all()
    Empleados_T = N_Emp_Total.objects.get(pk=1)

    return render(request, "respuesta.html",{'empleados':Empleados,'Datos_puestos':Datos_puestos,'Empleados_T':Empleados_T})

#COMPLETO >>>
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Crear una nueva instancia de Register y asignar los valores del formulario
            empleado = Datos_Empleados(nombre=form.cleaned_data['nombre'], apellido=form.cleaned_data['apellido'], puesto=form.cleaned_data['puesto'])
            # Guardar datos sino crearlo en la base de datos
            try:
                Nombre_Puesto = form.cleaned_data['puesto']
                Puesto_Empleados = N_Empleados_P.objects.get(puesto = Nombre_Puesto)
                Puesto_Empleados.n_emp = int(Puesto_Empleados.n_emp) + 1
                Puesto_Empleados.save()
            except N_Empleados_P.DoesNotExist:
                Crear_Puesto  = N_Empleados_P(puesto=form.cleaned_data['puesto'],n_emp=1)
                Crear_Puesto.save()

            try:
                Empleados_Base_Datos = N_Emp_Total.objects.get(pk=1)
                Empleados_Base_Datos.Empleados_Totales = int(Empleados_Base_Datos.Empleados_Totales) + 1
                Empleados_Base_Datos.save()
            except N_Emp_Total.DoesNotExist:
                empleados_totales = N_Emp_Total.objects.create(pk=1, Empleados_Totales=1)
                empleados_totales.save()
                
            
            empleado.save()

            # Redirigir a la página principal del sitio
            return redirect('../')
    else :
        form = RegisterForm()
    return render(request, 'registro.html', {"form":form})

def BusquedaDatos(request):
    if request.method == "POST":
        form = BusquedaForm(request.POST)
        if form.is_valid():
            Nombre_Buscado = form.cleaned_data['nombre']
            Apellido_Buscado = form.cleaned_data['apellido']
            Empleado_Buscado = Datos_Empleados.objects.get(nombre=Nombre_Buscado,apellido=Apellido_Buscado)
            return render(request,'Login.html',{'form':form ,'Datos':Empleado_Buscado})
    else:
        form = BusquedaForm()            
    return render(request, 'Login.html',{'form':form})








from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import Datos_Empleados, N_Empleados_P, N_Emp_Total
from django.contrib.auth.forms import AuthenticationForm

def search(request):
    search_query = request.GET.get('search_query')
    # Aquí implemente su lógica de búsqueda
    return render(request, 'search_results.html', {'search_query': search_query})



class BusquedaForm(forms.ModelForm):
    class Meta:
        nombre = forms.CharField(max_length=50)
        apellido =forms.CharField(max_length=50)
        model = Datos_Empleados
        fields = {'nombre','apellido'}



class RegisterForm(forms.ModelForm):
    class Meta:
        nombre= forms.CharField(max_length=50)
        apellido= forms.CharField(max_length=50)
        puesto= forms.CharField(max_length=100)
        model = Datos_Empleados
        fields = "__all__"

class RecipeForm(forms.ModelForm):
    class Meta:
        name = forms.CharField(max_length=200)
        ingredients = forms.CharField(max_length=3000)
        description = forms.CharField(max_length=5000)
      #  model = Recipe
        fields = "__all__"

class SearchForm(forms.Form):
    name = forms.CharField()
    ingredients = forms.CharField()
    description = forms.CharField()


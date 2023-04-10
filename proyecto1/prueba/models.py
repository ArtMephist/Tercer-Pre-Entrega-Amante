from django.db import models


# Create your models here.
class Datos_Empleados(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    

class N_Empleados_P(models.Model):  
    puesto = models.CharField(max_length=50)
    n_emp = models.CharField(max_length=50)

class N_Emp_Total(models.Model):
    Empleados_Totales = models.CharField(max_length=50)



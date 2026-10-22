from django.shortcuts import render
from datetime import date
from datetime import datetime

def primeraApp(request):
 NombreHtml = "home1.html"

 return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml})

def contacto(request):
 NombreHtml = "contacto.html"

 return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml})

def calendario(request):
 NombreHtml = "calendario.html"
 hoy = date.today()
 ahora = datetime.now()

 dia= hoy.day
 mes= hoy.month
 year= hoy.year

 ahora= datetime.now()
 return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml, 'dia': dia, 'mes': mes, 'year': year, 'hora': ahora})
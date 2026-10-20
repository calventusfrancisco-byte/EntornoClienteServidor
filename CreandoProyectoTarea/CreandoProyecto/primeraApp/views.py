from django.shortcuts import render
def primeraApp(request):
 NombreHtml = "home1.html"

 return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml})

def contacto(request):
 NombreHtml = "contacto.html"

 return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml})
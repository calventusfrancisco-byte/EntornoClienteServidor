from django.shortcuts import render
def homepage(request):
 NombreHtml = "PaginaPrincipal.html"

 return render(request, NombreHtml, {'html': NombreHtml})

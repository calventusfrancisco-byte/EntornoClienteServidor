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

def calendarioPersonalizado(request, dia, mes, year):
    NombreHtml = "calendario.html"
    hoy = date.today()
    ahora = datetime.now()

    ahora= datetime.now()
    return render(request, "PrimeraApp/" + NombreHtml, {'html': NombreHtml, 'dia': dia, 'mes': mes, 'year': year, 'hora': ahora})

def tresEnRaya(request):
    NombreHtml = "juego.html"
    ganador = 'Null'  # Definido aquí para que exista siempre en el contexto

    if request.method == 'POST':
        str_tablero = request.POST.get("tablero") #Seguramente tengas que tratar este string
        tablero = []
        for letra in str_tablero:
            if letra == '-':
                tablero.append(letra)
            elif letra == 'X':
                tablero.append(letra)
            elif letra == 'O':
                tablero.append(letra)

     
        posicion = int(request.POST.get("posicion"))
        print(posicion)
        turno = str(request.POST.get("turno"))
        
        if tablero[posicion] == '-':
            tablero[posicion] = turno
            if(turno == 'X'):
                turno = 'O'
            elif(turno == 'O'):
                turno = 'X'
       
        combinacionesGanadoras = [
            #Horizontales
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        
            #Verticales
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
        
            #Diagonales
            [0, 4, 8],
            [2, 4, 6]
        ]
       
        terminado = 0
        for combinacion in combinacionesGanadoras:
            if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] != '-':
                print('3 en raya')
                terminado = 1
                ganador = tablero[combinacion[0]]  # Asignamos el ganador cuando se cumple
            
        if '-' not in tablero:
            terminado = 2
            
        print("Terminado: " + str(terminado))
        mensaje = "Turno de " + turno

    else:
        
        tablero = ['-','-','-','-','-','-','-','-','-']
        turno = 'X'
        ganador = 'Null'
        mensaje = 'Turno de X'
        terminado = 0    
        print("El juego empieza, es el turno de: " + turno)
        
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
        'ganador': ganador
    }
    return render(request, "PrimeraApp/" + NombreHtml, contexto)
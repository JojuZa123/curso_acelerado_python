# Sesion 1

---
Listado de ejercicios

* ejercicio1.py
* 
'''
********** Curso de programacion acelerada de python **********
Date 07-10-2022
File: sesion1/ejercicio1.py
Autor: Programador Jose Juan Zurita Alvarez
Action: asignacion de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
productos_tabasco = ['cacao', 'coco', 'caña']
estados_cercanos = ['chiapas', 'campeche', 'veracruz']

print(
  nombre_estado,
  "es un estado que",
)
print("produce", productos_tabasco[0], "tiene una temperatura de ",
      promedio_temperatura)
print("y tiene una poblacion total de ",poblacion_total)
print("con", estados_cercanos[0], "colinda al sur", "y")
print("Tiene una superficie de ", superficie)

*ejercicio2.py
'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio2.py
Autor: programador Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''

lado=input("Ingrese la media del lado del cuadrado:")
lado=float(lado)
superficie =lado*lado
print("La superficie del cuadrado es:")
print(superficie)

*ejercicio3.py
'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio3.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''
horas = float(input("Introduce tus horas de trabajo:"))
coste = float(input("Introduce lo que cobras por hora:"))
horas_extra=float(input("Introduce tus horas extras:"))
subtotal=horas_extra*coste
paga = (horas * coste)+subtotal
print("Tu paga es", paga)

*ejercicio4.py
'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio4.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''
peso=input("¿Cual es tu peso en kg?")
estatura=input("¿Cual es tu estatura en metros?")
imc=round(float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es " + str(imc))

*ejercicio6.py
'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio6.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))

*ejercicio7.py

'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio7.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))






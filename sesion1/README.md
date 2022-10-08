# Sesion 1

---
Listado de ejercicios

* ejercicio1.py <br>

'''
********** Curso de programacion acelerada de python ********** <br>
Date 07-10-2022 <br>
File: sesion1/ejercicio1.py <br>
Autor: Programador Jose Juan Zurita Alvarez <br>
Action: asignacion de variables <br>
'''
nombre_estado = 'Tabasco'<br>
superficie = 25267<br>
poblacion_total = 2403000000 <br>
promedio_temperatura = 31.3  <br>
productos_tabasco = ['cacao', 'coco', 'caña']  <br>
estados_cercanos = ['chiapas', 'campeche', 'veracruz'] <br>

print(
  nombre_estado,
  "es un estado que",
) <br>
print("produce", productos_tabasco[0], "tiene una temperatura de ",
      promedio_temperatura) <br>
print("y tiene una poblacion total de ",poblacion_total) <br>
print("con", estados_cercanos[0], "colinda al sur", "y") <br>
print("Tiene una superficie de ", superficie) <br>

*ejercicio2.py <br>
'''
********* Curso de programacion acelerada en Python ********** <br>
Date 04-08-2022 <br>
File: sesion/ejercicio2.py <br>
Autor: programador Jose Juan Zurita Alvarez <br>
Action: superficie de un cuadrado <br>
'''

lado=input("Ingrese la media del lado del cuadrado:") <br>
lado=float(lado) <br>
superficie =lado*lado <br>
print("La superficie del cuadrado es:") <br>
print(superficie) <br>

*ejercicio3.py <br>
'''
********* Curso de programacion acelerada en Python ********** <br> <br>
Date 04-08-2022 <br>
File: sesion/ejercicio3.py <br>
Autor: Jose Juan Zurita Alvarez <br>
Action: superficie de un cuadrado <br>
'''
horas = float(input("Introduce tus horas de trabajo:")) <br>
coste = float(input("Introduce lo que cobras por hora:")) <br>
horas_extra=float(input("Introduce tus horas extras:")) <br>
subtotal=horas_extra*coste <br>
paga = (horas * coste)+subtotal <br>
print("Tu paga es", paga) <br>

*ejercicio4.py <br>
'''
********* Curso de programacion acelerada en Python ********** <br>
Date 04-08-2022 <br>
File: sesion/ejercicio4.py <br>
Autor: Jose Juan Zurita Alvarez <br>
Action: superficie de un cuadrado <br>
'''
peso=input("¿Cual es tu peso en kg?") <br>
estatura=input("¿Cual es tu estatura en metros?") <br> 
imc=round(float(peso)/float(estatura)**2,2) <br>
print("Tu indice de masa corporal es " + str(imc)) <br>

*ejercicio6.py <br>
'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio6.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

cantidad = float(input("¿Cantidad a invertir? "))<br>
interes = float(input("¿Interés porcentual anual? "))<br>
años = int(input("¿Años?"))<br>
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))<br>

*ejercicio7.py<br>

'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio7.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''
n = int(input("Introduce un número entero: "))<br>
suma = n * (n + 1) / 2<br>
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))<br>






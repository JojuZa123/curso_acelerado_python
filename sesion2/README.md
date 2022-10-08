# Sesion 2

---
Listado de ejercicios

*ejercicio8.py<br>
'''
********* Curso de programacion acelerada en Python ********** <br>
Date 04-08-2022<br>
File: sesion/ejercicio8.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

numero = int(input("Escriba un número(puede ser negativo, positivo o cero) "))<br>
if numero < 0:<br>
    print(f"¡Ha escrito el numero {numero} y es negativo")<br>
else:<br>
  print(f"¡Ha escrito el numero {numero} y es positivo")<br>
  
  *ejercicio9.py<br>
  '''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio9.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''
CONTRASEÑA="josejuan"<br>
contraseña=input("Escribe una contraseña")<br>
if contraseña==CONTRASEÑA:<br>
  print("CONTRASEÑA CORRECTA")<br>
else:<br>
  print("CONTRASEÑA INCORRECTA")<br>
  
  *ejercicio10.py<br>
  '''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio10.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''
n = int(input("Introduce un número entero: "))<br>
if n % 2 == 0:<br>
  print("El número " + str(n), " es par")<br>
else:<br>
  print("El número " + str(n) + " es impar")<br>
  
  *ejercicio11.py<br>
  '''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio11.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''
mes = int(input("Introduzca el mes del año: "))<br>

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10  or mes==12:
  print("El mes tiene 31 días.")<br>
elif mes == 2:<br>
  print("El mes tiene 28 o 29 días.")<br>
elif mes == 4 or mes == 6 or mes == 9 or mes ==11:<br>
  print("El mes tiene 30 días.")<br>
else:<br>
  print("Mes no válido.")<br>
  
  *ejercicio12.py <br>
  '''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio12.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

mes = int(input("Introduzca el mes de año: "))<br>
if 1 <= mes <= 12:<br>
  print("Se ha introducido un mes válido.")<br>
else:<br>
  print("El mes es incorrecto. Por defecto se elige Enero.")<br>
mes = 1<br>
print("Se utilizará mes:", mes)<br>

*ejercicio13.py<br>
'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio13.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

num = 1<br>
suma = 0<br>
while num <= 10: <br>
  suma += num<br>
print(suma)<br>
num += 1<br>

*ejercicio14.py<br>
'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio14.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

palabra=input("Escribre una palabra")<br>
num = 10<br>
for x in range(num):<br>
  print(palabra)<br>
  
  *ejercicio15.py<br>
  '''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio15.py<br>
Autor: Jose Juan Zurita Alvarez<br><br>
Action: superficie de un cuadrado<br>
'''

suma = <br>
for f in range(10):<br>
  valor = int(input("Ingrese valor:"))<br>
  suma = suma + valor<br>
print("La suma es")<br>
print(suma)<br>
promedio = suma / 10<br>
print("El promedio es:")<br>
print(promedio)<br>

*ejercicio16.py<br>

'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio16.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

n = int(input("Introduce la altura del triángulo (entero positivo): "))<br>
for i in range(n):<br>
  for j in range(i + 1):<br>
    print("*", end="")<br>
print("")<br>

*ejercicio17.py<br>
'''
********* Curso de programacion acelerada en Python **********<br>
Date 04-08-2022<br>
File: sesion/ejercicio17.py<br>
Autor: Jose Juan Zurita Alvarez<br>
Action: superficie de un cuadrado<br>
'''

numero = int(input("INGRESE UN NUMERO DEL 1 AL 10"))<br>
contador = 12<br>
acumulador = 0<br>
for x in range(contador):<br>
  acumulador = acumulador + 1<br>
  impresion = numero * acumulador<br>
  print(impresion)<br>



  




  

  

  

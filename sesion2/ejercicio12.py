'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio12.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''

mes = int(input("Introduzca el mes de año: "))
if 1 <= mes <= 12:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")
mes = 1
print("Se utilizará mes:", mes)

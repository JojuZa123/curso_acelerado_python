'''
********* Curso de programacion acelerada en Python **********
Date 04-08-2022
File: sesion/ejercicio16.py
Autor: Jose Juan Zurita Alvarez
Action: superficie de un cuadrado
'''

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
  for j in range(i + 1):
    print("*", end="")
print("")
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
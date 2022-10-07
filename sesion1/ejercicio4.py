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
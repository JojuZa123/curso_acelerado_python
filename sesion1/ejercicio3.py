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

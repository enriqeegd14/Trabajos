#from persona import Persona
from perros import Perro

"""nombre = input("Ingrese nombre aqui: ")
apellidos = input("Ingrese apellido aqui: ")
sexo = input("Ingrese sexo aqui: ")
edad = input("Ingrese edad aqui: ")
altura = input("Ingrese altura aqui: ")
color_ojos = input("Ingrese color de ojos aqui: ")
color_cabello = input("Ingrese color de cabello aqui: ")

persona = Persona(nombre, apellidos, sexo, edad, altura, color_ojos, color_cabello)
persona.mostrar_info()"""

nombre = input("Ingrese nombre aqui: ")
raza = input("Ingrese raza aqui: ")
sexo = input("Ingrese sexo aqui: ")
edad = input("Ingrese edad aqui: ")
color = input("Ingrese color aqui: ")

perros = Perro(nombre, raza, sexo, edad, color)
perros.mostrar_info()
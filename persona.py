class Persona:
    def __init__(self,nombre,apellidos,sexo,edad,altura,color_ojos,color_cabello):
        self.nombre = nombre
        self.apellidos = apellidos
        self.sexo = sexo
        self.edad = edad
        self.altura = altura
        self.color_ojos = color_ojos
        self.color_cabello = color_cabello
        
    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Apellidos: " + self.apellidos)
        print("Sexo: " + self.sexo)
        print("Edad: " + self.edad)
        print("Altura: " + self.altura)
        print("Color de ojos: " + self.color_ojos)
        print("Color de cabello: " + self.color_cabello)
        
    def edad_en_10_años(self):
        edad = int(self.edad)
        edad = edad + 10
        print("En diez años " + self.nombre + " tendra " + str(edad))
        
        
#pepito = Persona("Enrique","Cerecer Castro","Hombre","22","1.79","Cafe","Castaño")
#pepito.mostrar_info()
#pepito.edad_en_10_años()

nombre = input("Ingrese nombre aqui: ")
apellidos = input("Ingrese apellido aqui: ")
sexo = input("Ingrese sexo aqui: ")
edad = input("Ingrese edad aqui: ")
altura = input("Ingrese altura aqui: ")
color_ojos = input("Ingrese color de ojos aqui: ")
color_cabello = input("Ingrese color de cabello aqui: ")

persona = Persona(nombre, apellidos, sexo, edad, altura, color_ojos, color_cabello)
persona.mostrar_info()
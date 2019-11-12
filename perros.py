class Perro:
    def __init__(self,nombre,raza,sexo,edad,color):
        self.nombre = nombre
        self.raza = raza
        self.sexo = sexo
        self.edad = edad
        self.color = color
        
    def mostrar_info(self):
        print("Nombre: " + self.nombre)
        print("Raza: " + self.raza)
        print("Sexo: " + self.sexo)
        print("Edad: " + self.edad)
        print("Color: " + self.color)
class Persona:

    def __init__(self,edad):
        self.edad = edad

    def obtenerNombre(self):
        return self.nombre

    def obtenerEdad(self):
        return self.edad

persona1 = Persona(17)
persona2 = Persona(15)

print("")
print("Soy Carlos y tengo " , persona1.obtenerEdad() ," años")
print("Hola, yo me llamo Pablo y tengo ", persona2.obtenerEdad(), "años")



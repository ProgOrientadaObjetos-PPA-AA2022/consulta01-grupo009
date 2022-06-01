class Empleado():

    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

    def obtenerEdad(self):
        return self.edad

    def obtenerNombre(self):
        return self.nombre

    def obtenerOcupacion(self):
        return self.ocupacion

empleado1 = Empleado(31, "Leonardo", "Empleado")
empleado2 = Empleado(18, "Jose", "Desempleado")
empleado3 = Empleado(22, "Fabian", "Empleado")
empleado4 = Empleado(42, "Felipe", "Empleado")

print("")
print ("1era Persona - Nombre: " , empleado1.obtenerNombre(), " - Edad: " , empleado1.obtenerEdad(), " - Ocupacion: ", empleado1.obtenerOcupacion())
print ("2da Persona - Nombre: " , empleado2.obtenerNombre(), " - Edad: " , empleado2.obtenerEdad(), " - Ocupacion: ", empleado2.obtenerOcupacion())
print ("3era Persona - Nombre: " , empleado3.obtenerNombre(), " - Edad: " , empleado3.obtenerEdad(), " - Ocupacion: ", empleado3.obtenerOcupacion())
print ("4ta Persona - Nombre: " , empleado4.obtenerNombre(), " - Edad: " , empleado4.obtenerEdad(), " - Ocupacion: ", empleado4.obtenerOcupacion())
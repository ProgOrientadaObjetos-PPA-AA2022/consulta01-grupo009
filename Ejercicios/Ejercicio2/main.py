class Animal(object):

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def darNombreAnimal(self):
        return self.nombre

    def darEspecieAnimal(self):
        return self.especie

Perro = Animal("Firulais", "Perro")

print("")
print ("El animal es un: %s" % Perro.darEspecieAnimal())
print ("Dicho animal lleva por nombre: %s" % Perro.darNombreAnimal())
class Persona: #father class
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    """
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.nombre = nombre
    
    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self,edad):
        self.edad = edad
    """

class Empleado(Persona): #child class
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo = sueldo

    """
    @property
    def sueldo(self):
        return self.sueldo
    
    @sueldo.setter
    def sueldo(self,sueldo):
        self.sueldo = sueldo
    """

persona1 = Persona("Juan", 28)
empleado1 = Empleado("Pedro", 30, 1000)
print(persona1)
print(empleado1)
class Persona:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
    def __str__(self):
        return f'Hola me llamo {self.nombre} {self.apellido} mi edad es {self.edad} de la carrera {self.carrera}'
    
ejemplo = Persona("Oscar", "Nogales", 21, "desarollo en software")
print(ejemplo)
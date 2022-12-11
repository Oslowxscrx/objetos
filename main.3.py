class Creacion:
    nombre   = str
    apellido = str
    edad     = str
    carrera  = str
    semestre = str
    
    def __init__(self, nombre, apellido, edad, carrera, semestre):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        self.semestre = semestre
    
    def conversa(self):
        print("hola: " + self.nombre + self.apellido + " con " + self.edad + " anios de edad " + " bienvenido a la carrera de " + self.carrera + " de " + self.semestre )
        
ejemplo = Creacion("Oscar ", "Nogales", "20", "Desarrollo en Software", "2do nivel")
ejemplo.conversa()


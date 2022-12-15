class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
if __name__=='__main__':
    
    oscar = Persona("Oscar", "Nogales", 20)
    juan = Persona("Juan", "Urillo", 32)
    
    print(vars(oscar))
    
    
    
    
            
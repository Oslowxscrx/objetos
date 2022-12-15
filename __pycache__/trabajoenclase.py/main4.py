class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre    
        self.apellido = apellido
        self.edad     = edad
        
if __name__ == '__main__':
    Alisson = Persona(" Alisson", " Cumbajin", " 21")
    Lenin = Persona(" Lenin", " Montalvo", " 19")
    
    print(vars(Alisson))
    print(vars(Lenin))
    
class Persona:
    nombre   = str
    apellido = str
    edad     = int 
    
    def __init__(self, nombre, apellido, edad):
        self.nombre       = nombre
        self.apellido     = apellido
        self.edad         = edad 
    
        
    def conversar(self,otra_persona):
        return f"Hola{otra_persona.nombre}, me llamo {self.nombre}, tengo {self.edad} "
        
if __name__ == '__main__':
    Persona1 = Persona(" Jordan", " Gonzales",22)
    Persona2 = Persona(" Enzo", " Quishpe",20)
    

print(Persona1.conversar(Persona2))
print(Persona1.conversar(Alisson))
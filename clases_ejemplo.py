class Persona:
    def __init__(self,dni,direccion,nacionalidad):
        self.dni=dni
        self.direccion=direccion
        self.nacionalidad=nacionalidad

    def datos_persona(self):
        print(f"dni:{self.dni}, direccion:{self.direccion},nacionalidad:{self.nacionalidad}")

class Profesor(Persona):
    pass

#Heroe esta heredando todos los atributos y metodos de la clase persona,
#  Persona es clase padre de Heroe, Heroe es clase hija de Persona
class Heroe(Persona):

   
    #metodo constructor, se ejecuta automanticamente cuando la clase es 
    def __init__(self,name,power,nickname, dni, direccion, nacionalidad):
        super().__init__(dni, direccion, nacionalidad)
        self.nombre=name
        self.poder=power
        self.apodo=nickname
        self.edad=None
        self.ataque_principal(f"{self.nombre} {self.poder}")
        self.datos_persona()
    


    #metodos de la clase
    def ataque_principal(self,nombre:str):
        print(f"ataque principal: {nombre}")

    def datos_heroe(self):
        print(f"Nombre: {self.nombre}, Apodo: {self.apodo}, Poder:{self.poder}, Edad: {self.edad},dni:{self.dni}, direccion:{self.direccion},nacionalidad:{self.nacionalidad}")

    def setEdad(self,edad:int):
        self.edad = edad

    def getEdad(self):
        return self.edad    
     

#invocacion de clase
#spyderman es un objeto de la clase Heore, spyderman es una instancia de la clase heroe
spyderman=Heroe("Peter Parker","Super fuerza","Hombre araña","56454544H","Calle Ambar 88","UK")
spyderman.setEdad(20)
spyderman.datos_heroe()
#spyderman.datos_persona()

iroman=Heroe("Tony Stark","Millonario","Hombre de Acero","58787877T","Calle Olvido 77","EEUU")
iroman.setEdad(45)
iroman.datos_heroe()
#iroman.datos_persona()
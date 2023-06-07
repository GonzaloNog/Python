##Herencia

#Clase padre
class Animal:
    esta_vivo = True

    def __init__(self,edad):
        self.edad = edad
    
    def __str__(self):
        return f"Edad {self.edad}"
    
    def hablar(self): #Metodo generico vacio por ahora
        print("este es el metodo hablar")
    
    def moverse(self):
        print("este metodo es moverse")
    def describir(self):  #Método con una implementación
        print(f"Soy un animal del tipo: {type(self).__name__}")

class Perro(Animal):
    def __init__(self, edad, raza, duenio):
        # Alternativa 1
        # self.edad = edad
        # self.raza = raza
        # self.duenio = duenio

        # Alternativa 2
        # seria como si llamaras a...
        # ancestro.__init__(edad)
        super().__init__(edad)  # es equivalente a: self.edad = edad
        self.raza = raza
        self.duenio = duenio

    def hablar(self):  #Modifica el método generico y lo trabaja a su forma
        print("Guau!")

    def moverse(self):  #Lo mismo para este otro método
        super().moverse()
        print("Caminando con 4 patas")

    def dar_pata(self): #metodo especifico de la clase perro
        return "El perrito te ha dado la pata"
    
class Vaca(Animal):
    def hablar(self):
        print("Muuu!")

    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")

    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


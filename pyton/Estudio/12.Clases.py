### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin alias'):
        self.__name = name#propiedad privada
        self.surname = surname#propiedad publica
        self.fullname = f'{name} {surname} ({alias})' 
    
    def get_name(self):
        return self.__name

    def walk(self):
        print(f'{self.fullname} esta caminando')

my_person = Person('gonzalo','zeiss')
print(my_person.fullname)
my_person.walk()

my_other_person = Person("May",'alsina','gordita')
my_other_person.walk()
my_other_person.fullname = 'santi zeiss loquito'
my_other_person.walk()
print(my_other_person.get_name())


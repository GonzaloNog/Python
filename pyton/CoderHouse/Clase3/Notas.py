'''
En una lista encontraremos diferentes operaciones relacionales,
calcular mentalmente el resultado de cada expresión y almacenarlo en una nueva
lista que contendrá únicamente valores lógicos True y False.
'''
expreciones = [
    False == True, # False     True es == 1 y False es == 0
    10>=2*4, #True
    33/3 == 11, #True
    True > False, #True
    True*5 == 2.5*2#True
]
print(expreciones)

expreciones = [
    not False, #True
    not 3 == 5, #True
    33/3 == 11 and 5>2, # True
    True or False, # True
    True*5 == 2.5*2 or 123 >= 23,# True
    12>7 and True < False #False
]
print(expreciones)

nombre = str(input("Nombre "))
edad = int(input("edad "))

if nombre != '****' and edad > 5 and edad < 20 and len(nombre) >= 4 and len(nombre) <= 8 and (edad *3) > 35:
    print('Todo en orden')
else:
    print('Error')


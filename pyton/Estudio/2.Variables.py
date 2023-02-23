#Variables 

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

#concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print('Este es el valor de: ', my_bool_variable)

#funciones del sistema
print(len(my_string_variable))#len cuenta el largo

#Variables en una sola linea
name, surname, alias, age = "Gonzalo", "Zeiss", "Gonza", 27
print(name, surname, age, " y mi alias es ", alias)

#Inputs

'''
first_name = input('Cual es tu nombre: ')
age = input('Que edad tiene?')

print(first_name)
print(age)
'''

#Cambio tipo
name = 35
age = "Brais"
print(name)
print(age)

#Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(address)

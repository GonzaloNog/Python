### Loops ###

# While

my_condition = 0

while my_condition < 11:
    print(my_condition)
    my_condition += 1
else:
    print('Mi condicion es mayor o igual que 10')

my_condition = 0

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detiene la ejecucion')
        break
    print(my_condition)
print('La ejecucion continua')

# For

my_list = [10,40,50,70,23,53,26,2,1]

for element in my_list:
    print(element)

mi_tupla = (1,2,3,4)

for element in mi_tupla:
    print(element)

my_dict = {'Nombre':'Gonzalo','Apellido':'zeiss','Edad': 35, 1:'Python'}

for element in my_dict.values():
    print(element)

my_set = {'gonzalo','zeiss', 27}

for element in my_set:
    print(element)
else:
    print('El bucle for para diccionario a finalizado')

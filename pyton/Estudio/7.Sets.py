## sets ##

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {'gonzalo','zeiss',27}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('nog')

print(my_other_set)#no es una estructura ordenada

my_other_set.add('nog')

print(my_other_set)#no se puede repetir un valor

print('nog' in my_other_set)
print('noog' in my_other_set)

my_other_set.remove('nog')
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set

my_set = {'gonzalo','zeiss',27}

my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'c++','c#','Python'}

my_new_set = my_set.union(my_other_set)

print(my_new_set)

print(my_new_set.difference(my_set))

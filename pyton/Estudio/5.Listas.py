### Listas ###

my_list = list()
my_other_list = []

list = [1,2,3,4,5,6,7,8]

print(list.count(1)) #cuenta la cantidad de veces que se repite un valor
print(len(list))#cantidad de elementos

list_user = ['gonzalo', 'zeiss', 'gonza', 27]

name, lastname, apodo, ege = list_user

print(lastname)

funtions_list = ['hola','chau','casa']

funtions_list.append('tres')#agrega al final

print(funtions_list)

funtions_list.insert(2,'insert')#inserta en una posicion especifica

print(funtions_list)

funtions_list.remove('chau')#elimina el primer elemento que encuentra

print(funtions_list)

print(funtions_list.pop())#retira el ultimo valor, se le puede pasar un idix

print(funtions_list)

funtions_list_new = funtions_list.copy()#copia la lista

funtions_list_new.sort()#ordena la lista 

del funtions_list[1] #elimina el elemento sin retorno como con el pop()

print(funtions_list)

funtions_list.clear() #borra todo el contenido de la lista

print(funtions_list)
print(funtions_list_new)



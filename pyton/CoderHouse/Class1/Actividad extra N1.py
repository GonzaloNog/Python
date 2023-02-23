nota_1 = int(input("Nota uno "))
if(nota_1 < 0 or nota_1 > 10):
    print('Error: la nota tiene que ser entre 0 y 10')
    exit()
nota_2 = int(input("Nota dos "))
if(nota_2 < 0 or nota_2 > 10):
    print('Error: la nota tiene que ser entre 0 y 10')
    exit()
nota_3 = int(input("Nota tres "))
if(nota_3 < 0 or nota_3 > 10):
    print('Error: la nota tiene que ser entre 0 y 10')
    exit()

nota = ((20 * nota_1) + (30 * nota_2) + (50 * nota_3))/100
print(nota)

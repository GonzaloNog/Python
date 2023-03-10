'''
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''
a = 1
while a <= 100:
    if (a%3) == 0:
        if(a%5) == 0:
            print("fizzbuzz\n")
        else:
            print('fizz\n')
    elif (a%5) == 0:
        print('buzz\n')
    else:
        print(str(a) + '\n')
    a+=1
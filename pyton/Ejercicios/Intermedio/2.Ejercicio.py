'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
'''

def primo(numero):
    for index in range(2,numero):
        if((numero % index) == 0):
            return False
    return True

print(primo(6))
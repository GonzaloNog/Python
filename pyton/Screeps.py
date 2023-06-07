import sys 

print("hola")

#python Screeps.py "hola" 5

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = sys.argv[2]
    for r in range(repeticiones):
        print(texto)
else:
    print('Error de sistema')
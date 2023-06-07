BD = {}


        
def Registro():
        name = str(input("Ingrese nuevo nombre de usuario: "))
        if(name.count(" ")):
            print("El nombre de usuario no puede contener espacios")
            return
        if(len(name) < 6):
            print("El nombre de usuario tiene que tener almenos 6 caracteres")
            return
        if(name in BD):
            print("El nombre de usuario ya se encuentra en uso")
            return
        clave = str(input("Ingrese clave: "))
        if(clave.count(" ")):
            print("La clave no puede contener espacios")
            return
        if(len(clave) < 4):
            print("La clave tiene que tener almenos 4 caracteres")
            return

        BD[name] = clave

def MostrarUsuarios():
      print('USUARIOS')
      for element in BD:
        valor = BD[element]
        print(f'\t-Nombre de usuario: {element} Clave: {valor}')

def logue():
        name = str(input("Ingrese nombre de usuario: "))
        clave = str(input("Ingrese clave: "))  
        if(name in BD):
                if(BD[name] == clave):
                    print('Usuario logueado correctamente')
                else:
                    print('La clave es incorrecta')
        else:
              print('El usuario no se encuentra registrado')
               
        
                
def Main():
        comando = 'ok'
        while(comando != 'quit'):
                comando = str(input('Ingrese un comando(use "list" para ver la lista de comandos): '))
                if(comando == 'list'):
                        print('Lista de comandos:\n\t- list: muestra lista de comandos\n\t- registro: Registra un nuevo usuario\n\t- login: Permiti iniciar secion\n\t- quit: Cierra el programa\n\t- usuarios: Muestra todos los usuarios registrados')
                if(comando == 'registro'):
                        Registro()
                if(comando == 'usuarios'):
                      MostrarUsuarios()
                if(comando == 'login'):
                      logue()
                if(comando == 'quit'):
                        break
Main()




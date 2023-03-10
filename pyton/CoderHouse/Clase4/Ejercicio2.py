'''
Descripción de la actividad. 

Para aprobar un crédito, el cliente debe ser mayor de edad. 
Además, debe tener una antigüedad en el sistema financiero 
de mínimo 3 años y un ingreso mayor a 2500 dólares.  
En caso no tenga la antigüedad suficiente, su ingreso mensual 
debe ser como mínimo 4000 dólares. Si no cumple ninguna de las 
condiciones, no se aprueba el crédito

Datos iniciales
edad = 15
antigüedad = 10
ingreso = 1500


'''

edad = 15
antiguedad = 10
ingreso = 1500

if edad >= 18:
    if antiguedad >= 3:
        if ingreso >= 2500:
            print('Credito aprobado')
        else:
            print('Su ingreso no es suficiente para un credito')
    elif ingreso >= 4000:
        print('Su ingreso no es suficiente para un credito')
    else:
        print('No cumple los requisitos para un prestamo')
else:
    print('Tiene que tener mas de 18 a;os para poder sacar unc redito')
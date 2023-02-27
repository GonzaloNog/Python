### Funciones ###

def my_funtion():
    print('Esto es una funcion')

my_funtion()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(1,2.9)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

print(sum_two_values_with_return(10,5))

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname='gonzalo',name='zeiss')

def sum_two_values_with_default(first_value, second_value, alias = 'Sin alias'):
    return first_value + second_value

def print_upper_texts(*texts: str):
    for text in texts:
        print(text.upper())

print_upper_texts('Hola', 'como estas', 'bien')


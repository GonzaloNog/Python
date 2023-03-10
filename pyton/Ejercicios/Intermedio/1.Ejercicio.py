'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 '''
def anagrama(palabra_uno, palabra_dos):
    if(palabra_dos == palabra_uno):
      print('Son iguales')
      return False
    elif(len(palabra_uno) != len(palabra_dos)):
       print('No cuentan con la misma cantidad de caracteres')
       return False
    print(set(palabra_dos.lower()))
    print(set(palabra_uno.lower()))
    if(set(palabra_dos.lower()) == set(palabra_uno.lower())):
       print('iguales')
    
anagrama('Manco', 'mocan')
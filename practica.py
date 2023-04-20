"""1.1

1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
● nombre_heroe: un string con el nombre del personaje
La función deberá devolver a partir del parámetro recibido un nuevo string con
las iniciales del nombre del personaje seguidos por un punto (.)

● En el caso que el nombre del personaje contenga el artículo ‘the’ se
deberá omitir de las iniciales

● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
que lo tenga se deberá reemplazar por un espacio en blanco

La función deberá validar:

    ● Que el string recibido no se encuentre vacío
    Devolver ‘N/A’ en caso de no cumplirse la validación

Ejemplo de la salida de la función para Howard the Duck:
H.D.
"""

from data_stark import lista_personajes

def extraer_iniciales(lista_personajes,nombre_h:str):
    
    """
    Que hace: extraer las iniciales de un string 
    
    Que retorna: retorna un string (Las iniciales con .)
    
    Que recibe: recibe como parametro un string (El nombre a abreviar)
    """
    
    
    if len(nombre_h)>0:
        abreviado=''
        nombre_heroe=nombre_h.replace("-"," ")
        
        heroes=nombre_heroe.split()

        for nombre in heroes:
            if nombre.lower() == 'the' : #CUANDO COLOCO VARIACIONES DE THE SE PASA UNA
                heroes.remove(nombre)
            #print(heroes)  
        
            
                
        for iniciales in heroes:
            abreviado += iniciales[0].upper()+'.'
        
        return abreviado
    
    else:
        return "N/A"
        


"""1.2
1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como
parámetro:
● heroe: un diccionario con los datos del personaje

La función deberá agregar una nueva clave al diccionario recibido como
parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
llamar a la función ‘extraer_iniciales’
La función deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave ‘nombre’
En caso de encontrar algún error retornar False, caso contrario retornar True

"""


def definir_iniciales_nombre(heroes:dict,clave:str):
    
    if type(heroes) != dict:
        print("El argumento no es un diccionario")
        return False
    elif "nombre" not in heroes:
        print("La clave nombre no se encontro en el diccionario")
        return False
    else:
        heroes[clave]=extraer_iniciales(lista_personajes,heroes["nombre"])
        return True

definir_iniciales_nombre(lista_personajes[0],"Iniciales")




"""1.3 Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
parámetro:
● lista_heroes: lista de personajes
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
La función deberá iterar la lista_heroes pasándole cada héroe a la función
definir_iniciales_nombre.
En caso que la función definir_iniciales_nombre() retorne False entonces se
deberá detener la iteración e informar por pantalla el siguiente mensaje:
‘El origen de datos no contiene el formato correcto’
La función deberá devolver True en caso de haber finalizado con éxito o False
en caso de que haya ocurrido un error
"""
def agregar_iniciales_nombre(lista_heroes):
    
    if type(lista_heroes) != list:
        print("no es lista")
        
    if type(lista_heroes) ==list and len(lista_heroes) == 0:
        print("no tiene nada")
    
    for heroe in lista_heroes:
        
        fun_definir_iniciales=definir_iniciales_nombre(heroe,"Iniciales")
        
        if fun_definir_iniciales == True:
            return True
        elif fun_definir_iniciales==False:
            print("El origen de datos no contiene el formato correcto")
            break
        else:
            return False




"""1.4 Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
como parámetro:

La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes
seguido de las iniciales encerradas entre paréntesis ()
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
…
La función no retorna nada
"""
def stark_imprimir_nombres_con_iniciales(lista_heroes):
    
    if agregar_iniciales_nombre(lista_heroes)==True:
        for heroe in lista_heroes:
            heroe["nombre"]+=" "+"("+extraer_iniciales(lista_heroes,heroe["nombre"])+")"
            
            print("*",heroe["nombre"])

#stark_imprimir_nombres_con_iniciales(lista_personajes)

"""
2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como
parámetros:
● id_heroe: un entero que representa el identificador del héroe.
○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
2.3. Para probar la función podes pasarle cualquier entero
● genero_heroe: un string que representa el género del héroe ( puede
tomar los valores ‘M’, ‘F’ o ‘NB’)
La función deberá generar un string con el siguiente formato:

GENERO-000…000ID
Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
último el identificador recibido. Todos los códigos generados deben tener
como máximo 10 caracteres (contando todos los caracteres, inclusive el
guión). Se deberá completar con ceros para que todos queden del mismo
largo


Algunos ejemplos:
F-00000001
M-00000002
NB-0000010
La función deberá validar:
● El identificador del héroe sea numérico.
● El género no se encuentre vacío y este dentro de los valores esperados
(‘M’, ‘F’ o ‘NB’)
En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
correctamente retornar el código generado

"""
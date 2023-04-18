"""
Desafío #04:
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
un string, etc y que contendrá) y que es lo que retorna la función!

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
        
"""
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
    elif "nombre" not in heroes:
        print("La clave nombre no se encontro en el diccionario")
    else:
        heroes[clave]=extraer_iniciales(lista_personajes,heroes["nombre"])
    print(heroes)

definir_iniciales_nombre(lista_personajes[0],"Iniciales")
    





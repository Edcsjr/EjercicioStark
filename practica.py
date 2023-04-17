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
            if nombre.lower() =='the' in heroes:
                heroes.remove("the")
                
        for iniciales in heroes:
            abreviado += iniciales[0].upper()+'.'
        
        return abreviado
    
    else:
        return "N/A"
        
abreviatura=extraer_iniciales(lista_personajes,"efren david castaneda-soto in the python road")
print(abreviatura)

print(bool("abc"))
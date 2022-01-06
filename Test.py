from MangaLibrary import*
from typing import Iterable, List, Tuple, Any, Callable, Type, TypeVar, Dict

def test_lee_datos_manga(fichero: str) -> None:
    valores: List[DatosManga]
    valores=lee_datos_manga(fichero)
    
    print("*El numero total de datos de mangas es:",len(valores),'\n')
    print("*Mostrando los tres primeros registros leidos:",'\n',valores[0],'\n',valores[1],'\n',valores[2],'\n')
    print("*Mostrando los tres ultimos registros leidos:",'\n',valores[-3],'\n',valores[-2],'\n',valores[-1],'\n')

'''

'''
def test_filtra(fichero:str)->None:
    valores=lee_datos_manga(fichero)
    print("*Los mangas de género Drama son:")
    print("\n")
    imprime_lista(filtra(valores, "Drama"))
    print("\n")


def test_media(fichero:str)->None:
    valores=lee_datos_manga(fichero)
    print("La media es  {:.2f}".format(media_miembros(valores)))
    print("\n")


def test_mangaConMasCapitulos(fichero: str)->None:
    lm=lee_datos_manga(fichero)
    lr=MangasConMasCapitulos(lm)
    print("El manga que tiene mas capítulos es: ")
    imprime_lista(lr)
    

def test_ordena_filtra(fichero: str):
    valores=lee_datos_manga(fichero)
    imprime_lista(ordena_filtra(valores, "Adventure"))
    print('\n')
    
    
    
def test_agrupacion(nombreFichero):
    valores=lee_datos_manga(nombreFichero)
    da= agrupacion(valores)
    print("*Se agruparán las tuplas según los siguientes tipos:" + str(da.keys()))
    for clave in da.keys():
        lv= da[clave]
        print(clave+":",[(e[1],e[2]) for e in lv])
#    imprime_dict(diccionario_agrupado)
        
def test_capitulos_por_manga():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("Estos son los mangas con su número correspondiente de capítulos:")
    print("\n")
    imprime_dict(capitulos_por_manga(valores))


def test_genero_con_mas_capitulos():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("Este es el manga con más capítulos es:")
    print("\n")
    print(genero_con_mas_capitulos(valores))

def test_maximas_temporadas_por_tipo():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("Estos son el maximo numero de temporadas por tipo de manga:")
    imprime_dict(maximas_temporadas_por_tipo(valores))
    print("\n")
    
def test_max_seguidores_por_manga(nombreFichero):
    valores=lee_datos_manga(nombreFichero)
    print("Es:")
    imprime_dict(max_seguidores_por_manga(valores))
    print("\n")
    valores=lee_datos_manga(nombreFichero)
    print("Es:")
    imprime_dict(max_seguidores_por_manga2(valores))
    
def test_grafica():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print(grafica(valores))


'''
La ideal del código del menú está tomada de https://www.discoduroderoer.es/crear-un-menu-de-opciones-en-consola-en-python/
'''

if __name__ == '__main__': 

    salir = False
    opcion = 0
    nombre_fichero= './data/IS1_page_top50-100mangaMAL.CSV'
    #nombre_fichero= './data/dataset_prueba.csv'
 
    while not salir:
        print ("1. Leer dataset") 
        print ("2. Filtrado de lista")
        print ("3. Media")
        print ("4. Manga con más capítulos")
        print ("5. Orden y filtro")
        print ("6. Agrupación")
        print ("7. Capítulos por manga")
        print ("8. Género con más capítulos")
        print ("9. Máxima temporadas por tipo")
        print ("10. Máximo seguidores por manga")
        print ("11. Gráfica")
        print ("0. Salir del programa")
    
        opcion= int(input(("Elige una opcion: ")))

 
        if opcion == 1:
            test_lee_datos_manga(nombre_fichero)
        elif opcion == 2:
            test_filtra(nombre_fichero)
        elif opcion == 3:
            test_media(nombre_fichero)
        elif opcion == 4:
            test_mangaConMasCapitulos(nombre_fichero)
        elif opcion == 5:
            test_ordena_filtra(nombre_fichero)
        elif opcion == 6:
            test_agrupacion(nombre_fichero)
        elif opcion == 10:
            test_max_seguidores_por_manga(nombre_fichero)
        elif opcion == 0:
            salir = True
        else:
            print ("Introduce un numero entre 0 y 11")

        int(input(("Pulsa para seguir con el programa ")))

    print ("Fin")

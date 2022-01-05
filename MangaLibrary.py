
#from modulo1 import*

import csv
from  Test import*
import os #para evitar problemas con abrir archivos en mac o en windows
from collections import namedtuple 
from datetime import datetime
#from test.test__xxsubinterpreters import ListAllTests
#from matplotlib import pyplot as plt
from typing import Iterable, List, Tuple, Any, Callable, Type, TypeVar, Dict

K = TypeVar('K') 
V = TypeVar('V') 
E = TypeVar('E') 
R = TypeVar('R')

DatosManga = namedtuple("DatosManga", "Title,Synonims_Titles,Type,Published,Finished,Serialization,Score,Ranked,Popularity,Members,Favorites,Score_Voted_By,Volumenes,Chapter,Genre,Author,Adult_content")

'''
def test_lee_datos_manga(fichero):
    
    valores=lee_datos_manga(fichero)
    
    print("*El numero total de datos de mangas es:",len(valores),'\n')
    print("*Mostrando los tres primeros registros leidos:",'\n',valores[0],'\n',valores[1],'\n',valores[2],'\n')
    print("*Mostrando los tres ultimos registros leidos:",'\n',valores[-3],'\n',valores[-2],'\n',valores[-1],'\n')
'''

def imprime_lista(lista):
    for i in lista:
        print(i)
        print('\n')

def imprime_dict(d:Dict[Any,Any]) -> None:
    for i,j in d.items():
        print(i,j)
   # for clave in d.keys():
   #     print(clave)
     #   print(type(d.values()))
      #  if type(d.values) is List:
       # for valor in d.values():
       #     imprime_lista(valor)


def test_filtra(nombre_fichero):
    valores=lee_datos_manga(nombre_fichero)
    print("*Los mangas que son de Drama son:")
    print("\n")
    imprime_lista(filtra(valores, "Drama"))
    print("\n")


def lee_datos_manga(fichero:str)-> List[DatosManga]:
    
    ''' Lee el fichero y devuelve una lista con los datos de los mangas
        
        ENTRADA:
            Un fichero con los registros de los mangas
        
        SALIDA:
            @return mangas: lista de tuplas con los datos de los mangas
            @rtype mangas: [DatosManga(str, str, str, datetime, bool, float, int, int, int, int, int, int, int, str, str, bool)]
        
    '''

    datos_manga = []
    print(fichero)
    print(os.getcwd())
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for Title, Synonims_Titles, Type, Published, Finished, Serialization, Score, Ranked, Popularity, Members, Favorites, Score_Voted_By, Volumenes, Chapter, Genre, Author, Adult_content in lector:
            Volumenes=int(Volumenes)
            Chapter=int(Chapter)
            Published=datetime.strptime(Published, "%m/%d/%Y").date()
            Score=float(Score)
            Ranked=int(Ranked)
            Popularity=int(Popularity)
            Members=int(Members)
            Favorites=int(Favorites)
            Score_Voted_By=int(Score_Voted_By)
           # Adult_content=eval(Adult_content.capitalize())
            tupla=DatosManga(Title, Synonims_Titles, Type,Published, Finished, Serialization, Score, Ranked, Popularity, Members, Favorites, Score_Voted_By, Volumenes, Chapter, Genre, Author, Adult_content)
            datos_manga.append(tupla)
        return datos_manga


    
#BLOQUE1

#FUNCION 1
        
def filtra(ls: List[DatosManga], filtro) -> List[DatosManga]: 
    
    '''
    Función que devuelve una lista de tuplas con todos los mangas que cumplan el filtro
    
    ENTRADA:
        @param ls: Lista de tuplas que contiene los datos de los mangas
        @type ls: [DatosManga(str, str, str, datetime, bool, float, int, int, int, int, int, int, int, str, str, bool)]
        @param filtro: Genero específico con el que se filtran los mangas
        @type filtro: str
    
    SALIDA:
        @return: Lista de tuplas con el genero elegido y el titulo de los mangas
        @rtype: [(int, int)]
    '''
    
    lista=[(t.Genre, t.Title) for t in ls if filtro in t.Genre]
    return lista

def filtraCompresion(ls, filtro) -> List[Any]:
    
    '''
    Función que devuelve una lista de tuplas con todos los mangas que cumplan el filtro
    
    ENTRADA:
        @param ls: Lista de tuplas que contiene los datos de los mangas
        @type ls: [DatosManga(str, str, str, datetime, bool, float, int, int, int, int, int, int, int, str, str, bool)]
        @param filtro: Genero específico con el que se filtran los mangas
        @type filtro: str
    
    SALIDA:
        @return: Lista de tuplas con el genero elegido y el titulo de los mangas
        @rtype: [(int, int)]
    '''
    
    lista=[(t.Genre, t.Title) for t in ls if filtro]
    return lista

#FUNCION 3

def media(ls: List[DatosManga]) -> float:
    suma=0
    for t in ls:
        suma+=t.Members
        media=suma/len(ls)
    return media


#BLOQUE 2

#FUNCION 5

def MangaConMasCapitulos(ls: List[DatosManga]): 
    lista1=[(t.Chapter) for t in ls]
    lista2=[t for t in ls if t.Chapter==max(lista1)]
    return lista2

#FUNCION 6

def ordena_filtra(ls, filtro):
    lista_filtrada=[t for t in ls if filtro in t.Genre]
    return sorted(lista_filtrada, key=lambda x: x[9])

#FUNCION 7

def agrupacion(ls: List[any]) -> Dict[K,List[V]]:
    d=dict()
    for t in ls:
        clave=t.Type
        if clave not in d:
            d[clave]=[t]
        else:
            d[clave].append(t)
    return d


#BLOQUE 3

#FUNCION 8 

def capitulos_por_manga(ls):
    d=dict()
    for t in ls:
        clave=t.Genre
        if clave not in d:
            d[clave]=t.Chapter
        else:
            d[clave]+=t.Chapter
    return d
    
#FUNCION 11

def genero_con_mas_capitulos(ls):
    d= capitulos_por_manga(ls)
    return max(d.items(), key=lambda x: x[1])

#FUNCION 12

def maximas_temporadas_por_tipo(ls):
    d=dict()
    for t in ls:
        if t.Type not in d:
            d[t.Type]=t.Volumenes
        else:
            if d.get(t.Type) < t.Volumenes:
                d[t.Type]=t.Volumenes
    return d
 
#FUNCION 14
''' Función que devuelva un diccionario que hace corresponder a cada clave una lista ordenada con los n mayores o menores elementos 
que contienen dicha clave

las claves del diccionario serán el genero de las mangas y el valor una lista en orden descende según los seguidores 
'''


identity = lambda x:x

def grouping_reduce(iterable:Iterable[E], fkey:Callable[[E],K],op:Callable[[V,V],V], fvalue:Callable[[E],V]= identity) -> Dict[K, E]:
    a = {} 
    for e in iterable: 
        k = fkey(e)
        if k in a: 
            a[k] = op(a[k],fvalue(e)) 
        else:
            a[k] = fvalue(e) 
        return a
    
def grouping_list(iterable:Iterable[E], fkey:Callable[[E],K], fvalue:Callable[[E],V]=identity) -> Dict[K,List[V]]: 
    return grouping_reduce(iterable,fkey,lambda x,y:x+y, lambda x: [fvalue(x)])

def max_seguidores_por_manga(ls: List[any], n=3) -> Dict[Any,Any]:
    da=agrupacion(ls)
    print("*Se agruparán las tuplas según los siguientes tipos:" + str(da.keys()))
    for clave in da.keys():
        lv= da[clave]
        #print(clave+":",[(e[1],e[2]) for e in sorted(lv)[:n]])
        da[clave] = [(e.Title,e.Members) for e in sorted(lv, key=lambda x:x.Members)[:n]]
    return da

def max_seguidores_por_manga2(ls: List[DatosManga], n=3) -> Dict[Any,Any]:
    da=grouping_list(ls,fkey= lambda x:x.Genre)
    print("*Se agruparán las tuplas según los siguientes tipos:" + str(da.keys()))
    for clave in da.keys():
        lv= da[clave]
        #print(clave+":",[(e[1],e[2]) for e in sorted(lv)[:n]])
        da[clave] = sorted(lv, key=lambda x:x.Members)[:n]
    return da

    #FUNCION 15

def grafica(ls):
    titulo=[t.Title for t in ls]
    miembros= [t.Members for t in ls]
    
    '''
    plt.barh(range(6), miembros[:6], edgecolor='black')
    plt.yticks(range(6), titulo[:6], rotation=70)
    plt.title('Miembros por Manga')
    plt.xlim(min(miembros),60000)
    plt.show()
    '''


def test_filtra():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("*Los mangas que son de Drama son:")
    print("\n")
    imprime_lista(filtra(valores, "Drama"))
    
    print("\n")


def test_media():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("*La media de miebros en los Mangas es de",int(media(valores)))
    
    print("\n")


def test_maximo():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
    print("*El manga que tiene mas capítulos es:")
    print("\n")
  # print(maximo(valores))
    
    print("\n")

def test_ordena_filtra():
    valores=lee_datos_manga('../data/IS1_page_top50-100mangaMAL.csv')
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
        print ("4. Máximo")
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
            print("Opcion 3")
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
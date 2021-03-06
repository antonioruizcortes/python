
import csv
from  Test import*
from IterableUtils import*
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
'''
def imprime_manga(m: DatosManga) -> None:
    print ("Manga: {}")
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
        
def filtra(ls: List[Any], filtro: str) -> List: 
    
    '''
    Funci??n que devuelve una lista de tuplas con todos los mangas que cumplan el filtro
    
    ENTRADA:
        @param ls: Lista de tuplas que contiene los datos de los mangas
        @type ls: [DatosManga(str, str, str, datetime, bool, float, int, int, int, int, int, int, int, str, str, bool)]
        @param filtro: Genero espec??fico con el que se filtran los mangas
        @type filtro: str
    
    SALIDA:
        @return: Lista de tuplas con el genero elegido y el titulo de los mangas
        @rtype: [(str, str)]
    '''
    
    lista=[(t.Genre, t.Title) for t in ls if filtro in t.Genre]
    return lista



#FUNCION 3
'''
  devuelve la media de miembros por cada manga 
'''
def media_miembros(ls: List[DatosManga]) -> float:
    suma=0
    for t in ls:
        suma+=t.Members
        media=suma/len(ls)
    return media


#BLOQUE 2

#FUNCION 5
'''
devuelve la lista con las tupla de los mangas con m??ximo n??mero de cap??tulos  
'''

def MangasConMasCapitulos(ls: List[DatosManga]) -> List[DatosManga]: 
    lista1=[(t.Chapter) for t in ls]
    lista2=[(t.Title,t.Chapter) for t in ls if t.Chapter==max(lista1)]
    return lista2

#FUNCION 6

'''
devuelve una lista ... no se ....
'''
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



#devuelve un diccionario con el n??mero de capitulos de cada g??neros de manga. Tiene en cuenta los manga multig??nero
def capitulos_por_genero_manga(ls):
    d=dict()
    for t in ls:
        claves=str((t.Genre)).split("|")
        #print(claves)
       # print(claves)
        for clave in claves:
           # print("clave dentro multgenero",clave)
            if clave not in d:
                d[clave]=t.Chapter
            else:
                d[clave]+=t.Chapter
    return d

def genero_con_mas_capitulos(ls):
    d= capitulos_por_genero_manga(ls)
    return max(d.items(), key=lambda x: x[1])
#FUNCION 12

#devuelve un diccionario con el m??ximo n??mero de temporadas por tipo de manga
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
''' Funci??n que devuelva un diccionario que hace corresponder a cada clave una lista ordenada con los n mayores o menores elementos 
que contienen dicha clave

las claves del diccionario ser??n el genero de las mangas y el valor una lista en orden descende seg??n los seguidores 
'''

def max_seguidores_por_manga(ls: List[any], n=3) -> Dict[Any,Any]:
    da=agrupacion(ls)
    print("*Se agrupar??n las tuplas seg??n los siguientes tipos:" + str(da.keys()))
    for clave in da.keys():
        lv= da[clave]
        #print(clave+":",[(e[1],e[2]) for e in sorted(lv)[:n]])
        da[clave] = [(e.Title,e.Members) for e in sorted(lv, key=lambda x:x.Members)[:n]]
    return da

'''
Se inicializa el diccionario 'da' con los g??neros de los mangas disponibles en el dataset. 
Para ello usarmos la funcion 'grouping_list' que crea un diccionario a partir de una lista. 
Las claves de este diccionarios ser??n el G??nero (lambda x:x.Genre), y el valor, la lista (grupo) de
tuplas de cada g??nero. Se podr??a tomar parte de una tupla indic??ndolo el valor de 
par??metro por defecto de la funci??n grouping_list (lambda x:x)

'''
def max_seguidores_por_manga2(ls: List[Any], n=3) -> Dict[Any,Any]:
    da=grouping_list(ls,fkey= lambda x:x.Type)
    print("*Se agrupar??n las tuplas seg??n los siguientes tipos:" + str(da.keys()))
    for clave in da.keys():
        lv= da[clave]
        da[clave] = [(e.Title,e.Members) for e in sorted(lv, key=lambda x:x.Members)[:n]]
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

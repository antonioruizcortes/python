from MangaLibrary import*

def test_lee_datos_manga(fichero):
    
    valores=lee_datos_manga(fichero)
    
    print("*El numero total de datos de mangas es:",len(valores),'\n')
    print("*Mostrando los tres primeros registros leidos:",'\n',valores[0],'\n',valores[1],'\n',valores[2],'\n')
    print("*Mostrando los tres ultimos registros leidos:",'\n',valores[-3],'\n',valores[-2],'\n',valores[-1],'\n')

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
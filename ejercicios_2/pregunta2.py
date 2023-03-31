
lista=[]
listaUser=['Admin','Practicante','Bibliotecario']
libro1={
        'Nombre':"La leyenda de la peregrina",
        'Autor':"Carmen Posadas",
        'Categoria':"Autobiográfico",
        'Estado':"Disponible"                                        
        }
libro2={
        'Nombre':"La vida secreta de la mente",
        'Autor':"Mariano Sigman",
        'Categoria':"científico",
        'Estado':"Disponible"                                        
        }
libro3={
        'Nombre':"Bajo un cielo escarlata",
        'Autor':"Mark Sullivan",
        'Categoria':"Aventura",
        'Estado':"Disponible"                                        
        }
libro4={
        'Nombre':"Dune",
        'Autor':"Frank Herbert",
        'Categoria':"ciencia ficción",
        'Estado':"Disponible"                                        
        }

lista.append(libro1)
lista.append(libro2)
lista.append(libro3)
lista.append(libro4)


message="""
    1)Obtener la lista categoria de libros
    2)obtener nombres de los libros y autores
    3)Poder cambiar el estado de un libro a prestado
    4)lista de usuarios de la biblioteca
    5)Salir
"""
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar: "))
    if opcion==1:
            try:
                  
                 for i in lista:
                    print(i['Categoria'])
            except Exception as Error:
                print("sucedio un error",Error)
    if opcion==2:
            try:
                print("Nombre    Autor")
                print("******    *****")
                for i in lista:
                    print(i['Nombre'],"=>",i['Autor'])
                    
            except Exception as Error:
                    print("sucedio un error:",Error)
        
    if opcion==3:
            try:
                Nombre=input("mencione que libro desea poner en prestado: ")
                for i in lista:
                    if Nombre==i['Nombre']:
                         i['Estado']="Prestado"
                         print(i['Estado'])
                         print(i)
            except Exception as Error:
                print("sucedio un error")
    if opcion==4:
            try:
                for i in listaUser:
                    print(i) 
            except Exception as Error:
                print("sucedio un error: ",Error)
    if opcion==5:
        break
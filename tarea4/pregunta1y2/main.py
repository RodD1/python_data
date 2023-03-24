from lib.clases import Sorteo


message="""
    1)Agregar numero
    2)Mostrar lista
    3)Escoger posicion de una variable
    4)Salir
"""
sor=Sorteo()
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar: "))
    if opcion==1:
        try:
             
             rango=int(input("Digite el rango: "))
             
             sor.agregarNumeroAleatorio(rango)
             
        except Exception as Error:
                print("sucedio un error: ",Error)
        else:
            print("agregando numero")
    if opcion==2:
        
        try:
             sor.mostrarNumeroAleatorio()
             
        except Exception as Error:
                print("sucedio un error: ",Error)
    if opcion==3:
        try:
             valor=int(input("Digite la posicion del valor: "))
             sor.escogerNumAleatorio(valor)
             
        except Exception as Error:
                print("sucedio un error: ",Error)
    if opcion==4:
        print("Adios")
        break
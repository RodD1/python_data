from lib.clases import Registro

message="""
    1)Agregar mensaje
    2)Mostrar mensaje
    3)Salir
"""
reg=Registro()
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar: "))
    if opcion==1:
        try:
             mensaje=input("Digite el mensaje: ")
             reg.agregarMensaje(mensaje)
             
        except Exception as Error:
                print("sucedio un error: ",Error)
        else:
            print("agregando mensaje")
    if opcion==2:
        
        try:
             reg.mostrarMensaje()
             
        except Exception as Error:
                print("sucedio un error: ",Error)
    if opcion==3:
        print("Adios")
        break
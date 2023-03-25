#libreria
# pip install -U pyinstaller
#instalador de aplicacion
# pyinstaller main_ValidarNumero.py --onefile
from lib.clases import NumTelefonico


message="""
    1)Validar numero
    2)Salir
"""
nu=NumTelefonico()
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar: "))
    if opcion==1:
        try:
             numero=input("digite el numero telefonico: ")
             nu.ValidarNum(numero)
        except Exception :
                print("-no comienza con 9 asi que se valida que no es un numero telefonico de peru")
        
                
    if opcion==2:
        print("Adios")
        break
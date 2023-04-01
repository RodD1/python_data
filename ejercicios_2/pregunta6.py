

entrada={
    'nombre':"jorge perez",
    'escenario':"vip",
    'dia':"5 de abril",
    'cantidad':1,
    'Estado':"Disponible"
}
lista=[]
lista.append(entrada)

def buscarEntrada(pers):
    for i in lista:
        if pers==i['nombre']:
            print(i['nombre']," tiene una entrada para el dia ",i['dia']," en el escenario ",i['escenario']," con una cantidad de ",i['cantidad']," persona")
        else:
            print("No existe la persona ",pers," en el sistema")
def ValidarCantidadPase(num):
    for i in lista:
        if num==i['cantidad']:
            print("Se valido que tiene es correcto el numero de entrada de ",i['cantidad'])
def CambiarEstado(est):
    for i in lista:
        if est==i['nombre']:    
            i['Estado']="No disponible"
            print(i['Estado'])
            print(i)            


def main():
    
    nombre=input('nombre: ')
    num=int(input("numero de entrada: "))

    buscarEntrada(nombre)
    ValidarCantidadPase(num)
    CambiarEstado(nombre)
        
    
main()    
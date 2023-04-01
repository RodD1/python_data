

imprenta={
    'nombre':"Lorem Ipsum",
    'Realiza':"Es simplemente el texto de relleno de las imprentas y archivos de texto",
    'Comenzo':1500,
    'Popularizo':60,
    'Año':0   
}

lista=[]
lista.append(imprenta)

def buscar(nombre):
    for i in lista:
        if nombre==i['nombre']:
            print("Es correcto ",nombre)
        else:
            print("No es correcto ",nombre)
def Validar(num):
    for i in lista:
        if num==i['Comenzo']:
            print("Es correcto ",num)
        else:
            print("Es incorrecto ",num)
def Cambiar(est,est1):
    for i in lista:
        if est==i['Popularizo']:    
            i['Año']=est1
            print(i['Año'])
            print(i)            
        else:
            print("Es incorrecto, vuelva a intentar")

def main():
    
    nombre=input('Que es un simple texto de relleno de las imprentas y archivos de texto?: ')
    buscar(nombre)
    num=int(input("En que año inicio el Lorem Ipsum?: "))
    Validar(num)
    num1=int(input("En que año se popularizo por primera vez?: "))
    num2=int(input("En que año cree que tambien se hizo conocido?: "))
    Cambiar(num1,num2)
    
main()    
    
        
    
     
message="""
    1)Realizar un dibujo cuadrado
    2)iteraccion de una lista de numeros
    3)lista nombre y edad
    4)Salir
"""
while True:
    
    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            num=4
            for i in range(num):
                 
                 print("********")
        except Exception as Error:
                print("sucedio un error:",Error)
        
    if opcion==2:
            try:
                lista=[1,2,3,4,5,6,7,8,9,12]
                print(lista)
                for i in lista:
                    if (i % 2==0):
                        print("el numero",i," es el multiplo de 2")
                    else:
                         print("el numero ",i," no es multiplo de 2")
            except Exception as Error:
                print("sucedio un error")
    if opcion==3:
            try:
                lista=[["Roger",15],["Javier",25],["victor",36]]
                for i in lista:
                    if ((i[1])>17):
                        print(i,"Es mayor") 
                    else:
                         print(i,"no es mayor") 
            except Exception as Error:
                print("sucedio un error: ",Error)
    if opcion==4:
        break
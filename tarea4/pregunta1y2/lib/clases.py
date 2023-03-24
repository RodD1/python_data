from random import randint,random,uniform


class Sorteo:
    num=int
    listVaci=[]
   
    def agregarNumeroAleatorio(self,num):
        self.listVaci=[randint(1,40)for i in range(0,num)]

    def mostrarNumeroAleatorio(self):
        if len(self.listVaci)>0:
            for i,j in enumerate(self.listVaci):
                    print(i,"->",j)
        else:
            print("no se registro ningun numero")
    def escogerNumAleatorio(self,num):
         
        for i,j in enumerate(self.listVaci):
             if num==i:
                print(i,"->",j)     
                    

    


#c2=sorteo()
#p1=c2.agregarNumeroAleatorio(5)
#c2.mostrarNumeroAleatorio()
import re

class NumTelefonico:
   
    numero=str
    patron=r'^9\d{0}'
    patron2=r'^9\d*$'
    def ValidarNum(self,numero):
        lista=re.findall(self.patron,numero)
        lista2=re.findall(self.patron2,numero)
        li=list(lista2[0])
        try:
            if len(li)==9:
                for i in lista:
                    if i == '9':
                        print()
                        print("-si comienza con 9 el numero: ",lista2)
                        print("-numero validado")
                        print()    
            else:
                print("-No tiene la longitud de un numero telefonico ",lista2,"porque tiene ",len(li)," numeros")
        except Exception :
                print("-no comienza con 9 asi que se valida que no es un numero telefonico de peru")
            

c1=NumTelefonico()
p1="974562"
c1.ValidarNum(p1)            
                
            
       
        
        



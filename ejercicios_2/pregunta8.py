lista=[]
def GeneradorNum():
    
    for j in range(1,100001):
        if j > 1:
            contador=0
            i=2
            
            rest=j%i
            if rest==0:
                contador+=1
            i+=1
            if contador==0:
                lista.append(j)
                
            else:
                pass
        else:
                pass
    print(lista)            

GeneradorNum()
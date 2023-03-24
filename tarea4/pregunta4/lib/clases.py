
from datetime import datetime

class Registro:
    msg=str
    fecha=str(datetime.now())
    nombre_archivo="registro.txt"
    
    open("registro.txt", "w")
    
    def agregarMensaje(self,msg):
        with open(self.nombre_archivo, "a") as file:
            file.write(self.fecha+"-"+self.nombre_archivo+"-"+msg+"\n")
        
    def mostrarMensaje(self):
        try:
            with open(self.nombre_archivo) as file:
                print(file.read())

        except Exception as Error:
                print("sucedio un error: ",Error)

#c1=Registro()
#c2=c1.agregarMensaje("ro")
#c1.mostrarMensaje()
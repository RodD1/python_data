class Producto:
    
    nombre=""
    codigo=""
    
    def __init__(self,nombre,codigo) -> None:
        self.nombre=nombre
        self.stock=codigo
        
    pais="peru"
    Lote="0001"
    Año="2023"
    def __str__(self):
        return f'el producto es {self.nombre}: {self.pais}-{self.Lote}-{self.Año}'
    
class CarritoCompra:
    listaProductos=[]

    def __init__(self):
        self.listaProductos=[]
        
    def agregarProducto(self,Produc:Producto):
        self.listaProductos.append(Produc)
        
         
    def mostrarProductos(self):
        
        for i in self.listaProductos:
            print(i)
p=Producto("papa","1")
p1=CarritoCompra()
p1.agregarProducto(p)
p1.mostrarProductos()



class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    def __init__(self,id,nombre,precio,tipo,stock) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        print('Se ha creado el producto:', self.nombre)

    def __str__(self):
        return f'el producto {self.nombre} tiene como precio S/{self.precio}, es del tipo {self.tipo} y tiene un stock de {self.stock}'
class CarritoCompra:
    listaProductos=[]
    def __init__(self):
        self.listaProductos=[]
        
    def agregarProducto(self,product:Product):
        self.listaProductos.append(product)
        
         
    def mostrarProductos(self):
        for i in self.listaProductos:
            print(i)
        





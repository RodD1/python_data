class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} con {self.id}  de {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProdcut(self,num):
        for i,j in enumerate(self.listaProductos):
            if num==i:
                self.listaProductos.pop(i)
                print("se elimina :",j)
    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
        print(self.precioTotal)
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Calcular precio total
    4)Quitar producto
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto: ")
            precio=float(input("ingrese el precio del producto: "))
            tipo=input("ingrese el tipo del prodcuto: ")
            stock=int(input("ingrese el stock del prodcuto: "))
            release=int(input("ingrese el release del prodcuto: "))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print("sucedio un error",Error)
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        carrito.calcularPrecio()
    if opcion==4:
        idProduc=input("ingrese el id del producto:")
        carrito.quitarProdcut(idProduc)
    if opcion==5:
        break

from lib.clases import CarritoCompra
from lib.clases import Product

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=input("ingrese el precio del producto:")
            tipo=input("ingrese el tipo del prodcuto:")
            stock=input("ingrese el stock del prodcuto:")
            
            px=Product(id,name,precio,tipo,stock)
            carrito.agregarProducto(px)
        except Exception as Error:
                print("sucedio un error",Error)
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        break
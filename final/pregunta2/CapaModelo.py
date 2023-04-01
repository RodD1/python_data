import sqlite3
from Productos import Producto

conn=sqlite3.connect('demo.db')
#uri conection => uri conection to mysql with python
# sqlalchemy modulo simplifica eso
cur=conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS PRODUCTO(id INTERGER PRIMARY KEY,NOMBRE TEXT NOT NULL,PRECIO REAL NOT NULL)""")
conn.commit()

produc1=Producto('1','papa',2.5)
produc2=Producto('2','cebolla',4.5)
produc3=Producto('3','manzana',3.6)
produc4=Producto('4','pera',4.2)
produc5=Producto('5','platano',3.3)

Products={
    (produc1.id,produc1.nombre,produc1.precio),
    (produc2.id,produc2.nombre,produc2.precio),
    (produc3.id,produc3.nombre,produc3.precio),
    (produc4.id,produc4.nombre,produc4.precio)
}

cur.executemany("insert into producto VALUES (?,?,?)",Products)
conn.commit()

def Mostrar(producto):
    cur.execute("SELECT * FROM producto")
    producto = cur.fetchall()
    print(producto)


producto = cur.fetchall()

Mostrar(producto)
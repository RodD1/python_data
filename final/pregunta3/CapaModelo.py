import sqlite3
dat=[]
def insertar_tabla(db,tabla,elemnt):
    for i in elemnt:
        db.execute(f'insert into {tabla} (id,nombre,precio) values(?,?,?)',(i))
        db.commit()

def insertar(db):
    id=input("Digite el id: ")
    nombre=input("Digite el nombre: ")
    precio=input("Digite el precio: ")
    db.execute('insert into product (id,nombre,precio) values (?,?,?)', (id,nombre,precio))
    db.commit()


def mostrar(db,llave,tabla):
    db.row_factory = sqlite3.Row
    cursor = db.execute(f'select * from {tabla} where id = ?',(llave,))
    for row in cursor:
        print('{} - {} - {}'.format(row['id'], row['nombre'],row['precio']))
    return cursor.fetchone()

def principal():
    db=sqlite3.connect('productos.db')
    db.execute('drop table if exists product')

    db.execute('create table product(id int,nombre text,precio real)')

    insertar(db)
    insertar_tabla(db,'product',dat)
    mostrar(db,1,'product')
principal()
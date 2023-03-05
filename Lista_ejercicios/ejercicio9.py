lista1 =["javier",25,70386959]
lista2 =["pedro",45,72348552]
lista3 =["sergio",17,96341258]
lista4 =["rafael",26,85412637]
lista_dni=[70386959,72348554,85412637]
lista_vacia=[]
tupla=tuple(lista1+lista2+lista3+lista4)
print("quienes son mayores?: ")
print("\t")
if lista1[1]>17:
    print(lista1[0]," es mayor")
    if lista1[2]==lista_dni[0] or lista1[2]==lista_dni[1] or lista1[2]==lista_dni[2]:
        print(" se verifica dni")
        lista_vacia.append(["javier",25,70386959])
    else:
        print("no se verifico")
print("\t")
if lista2[1]>17:
    print(lista2[0]," es mayor")
    if lista2[2]==lista_dni[0] or lista2[2]==lista_dni[1] or lista2[2]==lista_dni[2]:
        print("se verifica dni")
        lista_vacia.append(["pedro",45,72348552])
    else:
        print("no se verifico")
print("\t")
if lista3[1]>17:
    print(lista3[0]," es mayor")
    if lista3[2]==lista_dni[0] or lista3[2]==lista_dni[1] or lista3[2]==lista_dni[2]:
        print("se verifica dni")
        lista_vacia.append(["sergio",17,96341258])
    else:
        print("no se verifico")
print("\t")
if lista4[1]>17:
    print(lista4[0]," es mayor")
    if lista4[2]==lista_dni[0] or lista4[2]==lista_dni[1] or lista4[2]==lista_dni[2]:
        print("se verifica dni")
        lista_vacia.append(["rafael",26,85412637])
    else:
        print("no se verifico")
print("\t")

print(lista_vacia)
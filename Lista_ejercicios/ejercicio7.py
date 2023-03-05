valor1=input("ingresa el primer valor: ")
valor2=input("ingresa el segundo valor: ")

print("los dos números son iguales?: ")
print("\t")
if valor1==valor2:
    print("-si son iguales")
else:
    print("-no son iguales")    
print("los dos números son diferentes?: ")
print("\t")
if valor1!=valor2:
    print("-si son diferentes")
else:
    print("-no son diferentes")    
print("el primero es mayor que el segundo?: ")
print("\t")
if valor1>valor2:
    print("-el primero es mayor que el segundo")
else:
    print("-el primero no es mayor que el segundo")    
print("el segundo es mayor o igual que el primero: ")
print("\t")
if valor2>valor1:
    print("-el segundo es mayor que el primero")
elif valor2==valor1:
    print("-son iguales")
else:
    print("-ninguna de las anteriores")  
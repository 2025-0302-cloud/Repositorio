lista_de_producto = []
lista_de_precios = []

contador = 0

cantidad_de_ventas = int(input("Ingrese la cantidad de ventas: "))
while contador < cantidad_de_ventas:
    producto = input("Ingrese el producto: ")
    precio = int(input("Ingrese el precio: "))
    lista_de_producto.append(producto)
    lista_de_precios.append(precio)
    contador += 1

indice = 0
count = 1
print()
print("-"*75)
print("                              Factura total")
print("-"*75)
for n in range(cantidad_de_ventas):
    print(f"{count}.{lista_de_producto[indice]}:${lista_de_precios[indice]}")
    indice += 1
    count += 1

valor_total = sum(lista_de_precios)
print()
print(f"Total a pagar: $ {valor_total}")

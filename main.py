
print("Bienvenido a tiendas D2")

Cliente = input("ingrese el nombre del cliente: \n").strip()

while True:
    vip_input = input("¿El cliente es VIP? (s/n o True/False): \n").strip().lower()
    if vip_input in ('true', 't', '1', 'yes', 'y', 'si', 's'):
        VIPstatus = True
        break
    elif vip_input in ('false', 'f', '0', 'no', 'n'):
        VIPstatus = False
        break
    else:
        print("Entrada inválida. Responda 's'/'n', 'si'/'no' o 'True'/'False'.")

while True:
    try:
        Cuantos_productos = int(input("ingrese cuantos productos distintos desea comprar: \n"))
        if Cuantos_productos < 0:
            print("Error: el número de productos no puede ser negativo.")
            continue
        break
    except ValueError:
        print("Error: debe ingresar un número entero válido para la cantidad de productos")



subtotal = 0.0
items_resumen = ""

for i in range(1, Cuantos_productos + 1):
    nombre = input(f"Producto {i} - ingrese el nombre: \n").strip()

    while True:
        try:
            cantidad = int(input(f"Producto {i} - ingrese la cantidad: \n"))
            if cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero válido para la cantidad")

    while True:
        try:
            precio = float(input(f"Producto {i} - ingrese el precio unitario: \n"))
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número válido para el precio")

    total_producto = cantidad * precio
    subtotal += total_producto
    items_resumen += f"- {nombre}: {cantidad} x {precio:.2f} = {total_producto:.2f}\n"

Descuento = 0.1
Descuento_aplicado = subtotal * Descuento if VIPstatus else 0.0
total = subtotal - Descuento_aplicado

print('\n-------------------- RECIBO ----------------------')
print(f"Cliente: {Cliente}")
print(f"VIP: {'Sí' if VIPstatus else 'No'}")
print('\nItems:')
print(items_resumen)
print(f"Subtotal: {subtotal:.2f}")
print(f"Descuento aplicado: {Descuento_aplicado:.2f}")
print(f"Total a pagar: {total:.2f}")
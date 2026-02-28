
print("Bienvenido a tiendas D2")

Cliente= str (input ("ingrese el nombre del cliente: \n"))
Producto= str (input ("ingrese el producto que desea comprar: \n"))


try:
    Cantidad= int (input ("ingrese la cantidad del producto que desea comprar: \n"))
except ValueError:
    print("Error: debe ingresar un número entero válido para la cantidad")
    Cantidad= int (input ("ingrese la cantidad del producto que desea comprar: \n"))


try:
    Precio= float (input ("ingrese el precio del producto: \n"))
except ValueError:
    print("Error: debe ingresar un número válido para el precio")
    Precio= float (input ("ingrese el precio del producto: \n"))

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

Descuento = 0.1
Precio_con_descuento = Precio * (1 - Descuento)
totalVIP = Cantidad * Precio_con_descuento
Descuento_aplicado = Cantidad * Precio * Descuento
subtotal = Cantidad * Precio

if VIPstatus:
    print("Gracias", Cliente, "por comprar en nuestra tienda y ser parte de nuestros clientes VIP")
    print("El subtotal es: ", subtotal)
    print("El total a pagar es: ", totalVIP, "por su estatus vip")
    print("El descuento aplicado es: ", Descuento_aplicado)  
else:
    print("Gracias", Cliente, "por comprar en nuestra tienda ")
    print("El total es: ", subtotal)
    print("El total a pagar si usted hiciera parte de nuestros clientes VIP seria de: ", totalVIP)
    print("El descuento aplicado seria de: ", Descuento_aplicado)
         


#Hello world!

#	Im a Coder currently learning Python and C++, with the objective of learning the Full Stack Development to make my own tools and maybe, if I feel like they are decent at the very least, to share them with the world

#	Im interested in developing software for music production and creation, this is a hobby I enjoy greatly and has teached a lot of things even beyond music
	
#	If you are to ask me anything about music in general expect me ranting 
	
#	I greatly enjoy learning new things, even if they are not part of my usual interest
	
#	90s JDM, 80s german, 60s American and series 2 car culture enthusiast 
	
#	In my free time I also enjoy reading books, my favorite genres are sci-fi, thriller and Distopian novels
	




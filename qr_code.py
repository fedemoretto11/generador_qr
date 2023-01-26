import qrcode



#Ingreso de link o lo que fuera para crear QR
link = input("Ingrese lo que desea generar en codigo QR: ")

# Pedido de version, tamaño y bordes
version_pedida = int(input("Ingrese la version que desea: "))
tamaño_pedido = int(input("Ingrese el tamaño que desea: "))
borde_pedido = int(input("Ingrese el borde que desea: "))


qr = qrcode.QRCode(version = version_pedida, box_size = tamaño_pedido, border = borde_pedido)
qr.add_data(link)
qr.make()

img = qr.make_image(fill_color = "black", back_color = "white")


# Guardado del QR como imagen con el nombre que ingrese el usuario
img.save(input("Ingrese el nombre con el que desea guardar: ") + ".png")



'''Menu de opciones
1. Ingresar producto bodega
2. Verificar los productos en bodega
3. Buscar un producto en la bodega
4. Editar un producto en la bodega
5. Retirar un producto de la bodega
6. Salir de la bodega'''

#Producto: nombre, codigo, decripcion, foto, precio, cantidadEnBodega,fechaEntradaBodega

opcion=0
print ("Tiendas el Gangazo\n********************")
print("1. Ingresar producto bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un producto en la bodega")
print("4. Editar un producto en la bodega")
print("5. Retirar un producto de la bodega")
print("6. Salir de la bodega\n********************")

productos = []

while(opcion != 6):
    producto={}
    opcion = int(input("Digita la opcion deseada: "))
    if opcion == 1:
        producto["nombre"] = input("Digita el nombre del producto: ")
        producto["codigo"] = int(input("Digita el codigo del producto: "))
        producto["descripcion"] = input("Digita la decripcion del producto: ")
        producto["foto"] = input("Adjunte el URL de la foto del producto: ")
        producto["precio"] = float(input("Digite el precio del producto: "))
        producto["cantidadEnBodega"] = int(input("Digite el stock del producto: "))
        producto["fechaEntradaBodega"] = (input("Digite la fecha del producto: "))
        
        productos = [producto]
    elif opcion ==2:
        for productoSeleccionado in productos: 
            print("--------------------------------------------------")
            print(f"El nombre del producto es: {productoSeleccionado['nombre']} \n El codigo del producto es: {productoSeleccionado['codigo']}\n La descripcion del producto es: {productoSeleccionado['descripcion']} \n La foto del producto es: {productoSeleccionado['foto']} \n El precio del producto es: {productoSeleccionado['precio']} \n La cantidad del producto es: {productoSeleccionado['cantidadEnBodega']} \n La fecha cuando entro a bodega es: {productoSeleccionado['fechaEntradaBodega']}")
            print("--------------------------------------------------")            
    elif opcion ==3:
        mostrarProducto = int(input("Escriba el codigo del producto el cual quiere buscar: "))
        for producto in productos:
            if mostrarProducto == producto['codigo']:
                print(f"Este es el producto el cual busca: {productoSeleccionado}")
            else:
                print("El producto no esta en la lista.")
    elif opcion ==4:
        pass
    elif opcion ==5:
        pass
    elif opcion ==6:
        pass
    else:
        print("Digite una opcion valida, vuelva a intentar la")
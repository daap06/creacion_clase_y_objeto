from instancias import Te


Solicitud = input("Desea generar un pedido: (S/N)").lower()
if Solicitud == "s":
    print("""Bienvenido, Nuestros té vienen en formatos de:
        
        300 gr precio $3.000
        500 gr precio $5.000
        
        por favor escoja un producto:
        1. Té negro
        2. Té verde
        3. Agua de hierbas.
        
        """)
    
producto = int(input("Escoja el producto:"))
formato = int(input("Escoja un formato: "))

    
pedido = Te()

print(pedido.precio_te(valor=formato , valor2=producto))

tiempo, recomendacion = Te.obtener_recomendacion(producto)

print(f"El sabor escogido es: {Te.sabores.get(producto, 'Sabor no válido')} ")
print(f"El formato es: {pedido.valida_formato(formato)} gramos.")
print(f"El Precio es: ${pedido.precio_te(formato, producto)}")
print(f"El tiempo de preparación es: {tiempo} minutos.")
print(f"La recomendación es: {recomendacion}")
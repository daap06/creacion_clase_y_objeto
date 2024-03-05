from te import Te   

te_negro = Te()
te_verde = Te()

tipo_1= type(te_negro)
tipo_2 = type(te_verde)

if tipo_1 == tipo_2:
    print("Ambos objetos son del mismo tipo")
else: 
    print("Los objetos no son del mismo tipo")
print(f"ESte es mi tipo: {tipo_1}")
print(f"ESte es mi tipo: {tipo_2}")

te_negro.precio_te
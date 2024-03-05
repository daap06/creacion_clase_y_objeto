###### Requerimiento 1 #######

class Te:
    sabores = {1: "Té negro", 2: "Té verde", 3: "Agua de hierbas"}
    peso_300 = 300
    peso_500 = 500
    precio_300 = 3000
    precio_500 = 5000

    
###### Requerimiento 2 #######

    @staticmethod
    def obtener_recomendacion(sabor):
        if sabor == 1: #Té negro
            return 3, " El té negro se recomienda consumir al desayuno."
        # return " El té negro tiene un tiempo de preparación de 3 minutos y se recomienda consumir al desayuno."
        elif sabor == 2:
            return 5, "El té verde se recomienda consumir al medio día."
        # return "El té verde tiene un tiempo de preparación de 5 minutos y se recomienda consumir al medio día."
        elif sabor == 3:
            return 6, "El agua de hierba sqe recomienda consumir al atardecer."
        # return "El agua de hierba tiene un tiempo de preparación de 6 minutos y se recomienda consumir al atardecer."
        else:
            return None, "Sabor no valido."

###### Requerimiento 3 #######    
    
    @staticmethod
    def precio_te(valor, valor2):  
        if valor == 300 and valor2 >0 and valor2 < 3:
            return Te.precio_300
        if valor == 500 and valor2 >0 and valor2 < 3:
            return Te.precio_500
        else:
            return "Formato invalido"

    @staticmethod
    def valida_formato(valor):
        if valor == int and valor == 300:
            return Te.peso_300
        elif valor == int and valor == 500:
            return Te.peso_500
        else:
            return "Formato invalido"
    
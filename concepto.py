lista_precio = [
    {1: "Té negro", "300": 3000, "500": 5000},
    {2: "Té negro", "300": 3000, "500": 5000},
    {3: "Té negro", "300": 3000, "500": 5000}]


# a = [{k,v} for k,v in lista_precio]
# print(a)

for i in lista_precio:
    # print(i)
    print(i.keys())
    # print(lista_precio[i])
    
    for k,v in i.items():
        print(k)
    #     print(k,v)
    # if 1 in lista_precio[0] and "300" in lista_precio[0]:
    #     print("te encontre",lista_precio[0][1])
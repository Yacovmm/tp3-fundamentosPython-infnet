lista = ["yacov","luciano","thiago","nome4","nome5","nome6","nome7","nome8","nome9"]
lista2 = [1, 2, 3, 4, 5]

for i, word in lista:   
  a = word[::-1]
  lista[i] = a
  
  

print(lista)


lista = ["yacov","luciano","thiago","nome4","nome5","nome6","nome7","nome8","nome9"]

lista = list(map(lambda x: x[::-1], lista))

print(lista)


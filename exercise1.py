lista = []
for i in range(1, 6):
  lista.append(i)
print(lista)

if 3 and 6 in lista:
  lista.remove(3, 6)

print(lista)
print (len(lista))

lista[-1] = 6
print(lista)

  
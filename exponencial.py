base = int(input("Entre com o valor da base: "))
exp  = int(input("Entre com o valor do expoente: "))
cont = exp
resultado = 1
while cont > 0:
  resultado = resultado * base
  cont = cont - 1

print(resultado)

#recursividade
def pot (base, exp):
  if exp == 0:
    return 1
  return base * pot(base, exp - 1)


print(pot(2,10))
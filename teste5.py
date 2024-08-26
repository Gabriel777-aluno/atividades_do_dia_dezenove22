def mdc(a, b):
 if b == 0:
  return a
 else:
  return mdc(b, a % b)
num1 = int(input("digite um"))
num2 = int(input("Digite outro número:"))
resultado = mdc(num1, num2)
print("MDC:", resultado)
#aqui ele imprime na tela o minimo divisor

#na 1 e 5 ele define e faz a parte algebrica 

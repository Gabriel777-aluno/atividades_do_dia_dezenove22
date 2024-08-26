def maior3(a, b, c):
  #ele vai pedir
  if a >= b and a >= c:
   return a
  elif b >= c:
   return b
  else: return c
n1=int(input("digite um numero"))
n2=int(input("digite um numero"))
n3=int(input("digite um numero"))
resultado = maior3(n1,n2,n3)
print(resultado)
#ele vai comparar e tirar o maior dos numeros e imprimir

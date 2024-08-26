def converter_quilometros_para_metros(quilometros):
 metros = quilometros * 1000
 return metros

#aqui ele faz o calculo

try:
  
  quilometros = float(input("Digite a distância em quilômetros:"))
  metros = converter_quilometros_para_metros(quilometros)
  print("metros:", metros)
except ValueError:
 print("Entrada inválida!")

 #vai te pedir a distancia,e o try é utilizado para envolver código que pode gerar exceções, caso tenha exceção ele retorna entrada invalida.
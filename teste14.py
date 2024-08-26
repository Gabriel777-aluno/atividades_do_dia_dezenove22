numeros = [] 
for i in range(10):
    try:
     numero = int(input("Digite um número inteiro: "))
     numeros.append(numero)
      #caso não for um número
    except ValueError: 
          print("Entrada inválida!!!") 
soma = sum(numeros) 
media = soma / len(numeros) 
print("soma", soma) 
print("media", media)

#'1 a 5' o código recebe os elementos
#'6 a 7' o código imprime um mensagem de erro caso não houver um número inserido
#'10 a 15' imprime na tela os resultados para o usuário

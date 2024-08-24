import random


def imprime_cartela(cartela):
  print("[", end="")
  for int in cartela:
    if int == cartela[len(cartela)-1]:
      print(int,end="")
    else:
      print(int,end=", ")
  print("]")

i = 0
contador = 0
cartela = []

while(i < 5):
  num = random.randint(1,75)
  cartela.append(num)
  i += 1

print("Sua cartela: ", end="")
imprime_cartela(cartela)

while(1):
  num_sorteado = random.choice(cartela)
  print("Tente adivinhar o numero sorteado: ", end="")
  while(1):
    tentativa = int(input())
    if tentativa != num_sorteado:
      print("Numero errado! Tente novamente: ", end="")
    else:
      break
  cartela.remove(num_sorteado)
  if len(cartela) == 1:
    break
  print("Voce acertou! Numeros restantes na cartela: ", end="")
  imprime_cartela(cartela)
  contador += 1
print("Parabens! Você concluiu sua cartela em", contador, "sorteios")

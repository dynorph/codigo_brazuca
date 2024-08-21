import random

numero = random.randint(1, 100)
print("Estou pensando em um numero entre 1 e 100. Voce consegue adivinha-lo?")
while(1):
  tentativa = int(input())
  if (tentativa > numero):
    print("O numero que eu estou pensando e menor, tente novamente")
  elif (tentativa < numero):
    print("O numero que eu estou pensando e maior, tente novamente")
  else:
    break
print("Parabens! Voce adivinhou o numero!")

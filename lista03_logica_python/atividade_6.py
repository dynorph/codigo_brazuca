frase = input("Insira uma frase: ")
contador = 0

for char in frase:
  if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    contador = contador + 1
print("Vogais:", contador)

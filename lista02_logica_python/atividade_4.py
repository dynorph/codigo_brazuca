palavra = input("Insira uma palavra: ")

if palavra == palavra[::-1]:
  print("E um palindromo")
else:
  print("Nao e um palindromo")

lista = []
contador = 1
while contador == 1:
  print("LISTA DE COMPRAS")
  print("1. Adicionar item")
  print("2. Imprimir lista")
  print("3. Sair")
  escolha = int(input())
  if escolha == 1:
    lista.append(input("Escreva o item que deseja adicionar: "))
    print("Item adicionado com sucesso!")
  else:
    if escolha == 2:
      for str in lista:
        print(str)
    else:
      if escolha == 3:
        contador = 0
      else:
        print("ERRO: Escolha invalida, tente novamente")
lista = []
soma = 0
while(1):
  num = int(input("Insira numeros para compor uma lista (-1 para encerrar): "))
  if num == -1:
    break
  lista.append(num)
maior = lista[0]
menor = lista[0]
for i in range(len(lista)):
  if lista[i] > maior:
    maior = lista[i]
  if lista[i] < menor:
    menor = lista[i]
  soma += lista[i]
print("Maior numero da lista:", maior)
print("Menor numero da lista:", menor)
print("Media dos numeros da lista:", soma/len(lista))

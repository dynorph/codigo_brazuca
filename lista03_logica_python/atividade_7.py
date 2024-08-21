soma_nota = 0
contador = 0
while(1):
  nota = float(input("Insira notas (-1 para encerrar): "))
  if nota == -1:
    break
  soma_nota += nota
  contador += 1
media = soma_nota / contador
print("Media: ", format(media, ".2f"))

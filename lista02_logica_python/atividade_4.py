celsius = int(input("Qual a temperatura atual? "))

if celsius > 30:
  print("Esta quente")
else:
  if celsius > 15 & celsius < 30:
    print("Esta agradavel")
  else:
    print("Esta frio")
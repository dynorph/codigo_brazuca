def par(num):
  if num % 2 != 0:
    return False
  return True

num = int(input("Insira um numero: "))
if par(num):
  print("Par")
else:
  print("Impar")

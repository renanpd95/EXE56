import os

n = int(input("Digite um número: "))
os.system('clear')

if(n % 2 == 0):
  print("Número é Par")
else:
  print("Número é Impar")
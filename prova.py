import random as rd

def Cross(tam):
  cromossomo = []
  i = 0
  while i < tam:
    gene = rd.randint( 0,1)
    cromossomo.append(gene)
    i = i+1
  return cromossomo

vtrben = [3, 3, 2, 4, 2, 3, 5, 2]
vtrpeso = [5, 4, 7, 8, 4, 4, 6, 8]

size= 8

while True:
  i=0
  Beneficio = 0
  Peso = 0
  cromossomo = getCromossomo(size)
  while i < size:
    if cromossomo[i] == 1:
      Beneficio = Beneficio + vtrbeneficio[i]
      Peso = Peso + vtrpeso[i]
    i = i + 1
  if vlrPeso <= 25:
    print("peso: ", Peso)
    break

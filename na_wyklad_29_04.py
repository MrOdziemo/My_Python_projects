lista = [[1,2,7], [-1,2,4], [1,2], [3,-7,-8,-10]]

def suma_jeden (lista):
  help_list = []
  for element in lista:
    help_list.append(sum(element))
  maks = max(help_list)
  return maks

def suma_dwa (lista):
  maks = max(list(map(sum, lista)))
  return maks

def elementy_wieksze_od_zera_jeden(lista):
  pomocna_lista = []
  for element in lista:
    for elemencik in element:
      if elemencik > 0:
        pomocna_lista.append(elemencik)
  return pomocna_lista

def pomoc (lista):
  wypakowanie = []
  for element in lista:
    for elemencik in element:
        wypakowanie.append(elemencik)
  return wypakowanie

def elementy_wieksze_od_zera_dwa (pomoc, lista):
  zmienna = list(filter(lambda x: x>0, pomoc(lista)))
  return zmienna

print(suma_jeden(lista))
print(suma_dwa(lista))
print(elementy_wieksze_od_zera_jeden(lista))
print(elementy_wieksze_od_zera_dwa(pomoc, lista))
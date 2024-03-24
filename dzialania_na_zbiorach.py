list_one = ["Jakub", "Jakub", "Wiktoria", "Klaudia", "Karol", "Karol", "Zbigniew", "Kamil", "Adam"]
list_two = ["Jakub", "Kamil", "Wiktoria", "Klaudia", "Karol", "Klaudia", "Zbigniew", "Kamil", "Józef"]

#Suma zbiorów z powtórzeniami
print("Suma dwóch zbiorów z powtórzeniami")
def sum_list_one(list_one, list_two):
    suma = []
    for sum_one in list_one:
        suma.append(sum_one)
    for sum_two in list_two:
        suma.append(sum_two)

    return suma

print(sum_list_one(list_one, list_two))

#Suma zbiorów bez powtózeń
print("\nSuma dwóch zbiorów bez powtózeń")
def sum_list_two(list_one, list_two):
    suma = []
    for sum_one in list_one:
        suma.append(sum_one)
    for sum_two in list_two:
        suma.append(sum_two)
    convert = set(suma)
    convert = list(convert)

    return convert

print(sum_list_two(list_one, list_two))

#Iloczyn zbiorów
print("\nIloczyn dwóch zbiorów(pętlą for, zawiera duplikaty!)")
def together_list_one(list_one, list_two):
    together = []
    for sum_one in list_one:
        if sum_one in list_two:
            together.append(sum_one)

    return together

print(together_list_one(list_one, list_two))

#Iloczyn zbiorów
print("\nIloczyn dwóch zbiorów(set)")
def together_list_two(list_one, list_two):
    lis1 = set(list_one)
    list2 = set(list_two)
    together = lis1 & list2
    list_together = list(together)

    return list_together

print(together_list_two(list_one, list_two))

#Różnica zbiorów
print("\nRóżnica zbioru list_one od list_two")
def minus_list_one(list_one, list_two):
    list1 = set(list_one)
    list2 = set(list_two)
    minus = list1 - list2
    list_minus = list(minus)

    return list_minus

print(minus_list_one(list_one, list_two))

#Różnica zbiorów
print("\nRóżnica zbioru list_two od list_one")
def minus_list_two(list_one, list_two):
    list1 = set(list_one)
    list2 = set(list_two)
    minus = list2 - list1
    list_minus = list(minus)

    return list_minus

print(minus_list_two(list_one, list_two))

#Różnica symetryczna zbiorów
print("\nRóżnica symetryczna zbiorów")
def minus_list_two(list_one, list_two):
    list1 = set(list_one)
    list2 = set(list_two)
    simetric = list2 ^ list1
    list_simetric = list(simetric)

    return list_simetric

print(minus_list_two(list_one, list_two))
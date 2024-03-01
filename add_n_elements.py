my_list = []
number = input("Ile liczb chcesz dodać?: ")
numbers_elements = int(number)

if(numbers_elements <= 0):
    print("Musisz podac liczbę elementów większą niż zero.")

for sum_number in range(0, numbers_elements, 1):
    add = input("Podaj liczbę: ")
    ad = int(add)
    my_list.append(ad)

print("Podane liczby do dodania:", my_list)

suma = sum(my_list[:])
print("Suma liczb to:", suma)
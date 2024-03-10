my_list = []
number = input("How numbers you want add?: ")
numbers_elements = int(number)

if(numbers_elements <= 0):
    print("You must enter number bigger of zero.")

for sum_number in range(0, numbers_elements, 1):
    add = input("You enter number: ")
    ad = int(add)
    my_list.append(ad)

ads = 1

for i in my_list:
    ads = ads * i

print(ads ** (i/numbers_elements))
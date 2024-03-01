numberone = input("Podaj pierwszą liczbę: ")
number_one = int(numberone)
numbertwo = input("Podaj drugą liczbę: ")
number_two = int(numbertwo)

while(number_one != number_two):
    if(number_one > number_two):
        number_one = number_one - number_two
    elif(number_one < number_two):
        number_two = number_two - number_one
    else:
        print("Podane dane są nieprawidłowe")

print("Największy wspólny dzielnik to", number_one)
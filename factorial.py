def factorial(x):
    if(x == 0):
        return 1
    else:
        return(x * factorial(x - 1))
    
number = input("Podaj liczbę do obliczenia jej silni: ")
x = int(number)

print(factorial(x))
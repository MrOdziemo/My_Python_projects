print('Witaj w przeliczniku temperatur!')
skala = input("Podaj skale , na jaką ma zostać wykonane przeliczenie ('C na F', 'F na C', 'C na K', 'K na C', 'F na K', 'K na F')\n")
if str(skala) == 'F na C':
    temperatura_F = input('Podaj temperaturę w skali Fahrenheita\n')
    temperatura_F = int(temperatura_F)
    temperatura_C = (temperatura_F - 32) / 1.8
    print(temperatura_C, 'Celcjusza')
    print('Dziękuję za skorzystanie z programu')
elif str(skala) == 'C na F':
    temperatura_C = input('Podaj temperature w skali Celcjusza\n')
    temperatura_C = int(temperatura_C)
    temperatura_F = (temperatura_C * 1.8) + 32
    print(temperatura_F, 'Fahrenheita')
    print('Dziękuję za skorzystanie z programu')
elif str(skala) == 'C na K':
    temperatura_C = input('Podaj temperature w skali Celcjusza\n')
    temperatura_C = int(temperatura_C)
    temperatura_K = temperatura_C + 273.15
    print(temperatura_K, 'Kelvina')
    print('Dziękuję za skorzystanie z programu')
elif str(skala) == 'K na C':
    temperatura_K = input('Podaj temperaturę w Kelvinach\n')
    temperatura_K = int(temperatura_K)
    temperatura_C = temperatura_K - 273.15
    print(temperatura_C, 'Celcjusza')
    print('Dziękuję za skorzystanie z programu')
elif str(skala) == 'F na K':
    temperatura_F = input('Podaj temperaturę w Fahreheitach\n')
    temperatura_F = int(temperatura_F)
    temperatura_K = (temperatura_F - 32) / 1.8 + 273.15
    print(temperatura_K, 'Kelvina')
    print('Dziękuję za skorzystanie z programu')
elif str(skala) == 'K na F':
    temperatura_K = input('Proszę podać temperaturę w Kelvinach\n')
    temperatura_K = int(temperatura_K)
    temperatura_F = (temperatura_K - 273.15) * 1.8 + 32
    print(temperatura_F, 'Fahrenheita')
    print('Dziękuję za skorzystanie z programu')
else:
    print('Nie właściwa opcja')
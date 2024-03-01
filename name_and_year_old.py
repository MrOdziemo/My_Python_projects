name = input("Podaj swoje imię: ")
year_old = input("Podaj swój wiek: ")
year = int(year_old)

if(year <= 0):
    print("Wiek nie może być ujemny")
elif(year < 12):
    print("Witaj " + name + " oraz pozdrawiam. Jesteś dzieckiem.")
elif(year < 18):
    print("Witaj " + name + " oraz pozdrawiam. Jesteś młodzieńcem.")
else:
    print("Witaj " + name + " oraz pozdrawiam. Jesteś dorosły.")
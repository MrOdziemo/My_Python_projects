from random import choice

print("Witaj w grze 'wisielec'!\n\n"
      "Opis gry:\n"
      "-Zadaniem gracza jest odgadnąć słowo za pomocą podawaia liter wyrazu.\n\n"
      "Zasady:\n"
      "-gracz ma 10 szans. Jeśli poda on złą literę, traci jedną szanse.\n"
      "-gracz wygrywa w momencie zgadnięcia wszystkich liter wyrazu.\n"
      "-gracz przegrywa w momencie wykorzystania wszystkich możliwych szans.\n\n")

while(True):
    verbs = ["python", "programowanie", "zmienne", "obiektowość", "asercja", "środowisko"]
    draw_verb = choice(verbs)
    number_verb = int(len(draw_verb))
    list_verb = list(draw_verb)
    how_verb = "_" * number_verb
    antilist_verb = list(how_verb)

    lives = 10

    while(lives > 0):
        if(list_verb == antilist_verb):
            y = "".join(antilist_verb)
            print("Brawo! Odgadłeś wyraz '" + y + "' oraz wygrałeś grę!")

            answer = input("Czy chcesz zagrać jeszcze raz?(tak lub nie): ")
            if answer == "tak":
                break
            elif answer == "nie":
                exit()

        print("Twoja liczba szans:", lives)
        print("Odgadywane słowo:", antilist_verb)

        letter = input("Podaj literę: ")

        if letter in list_verb:
            print("Litera '" + letter + "' znajduje się w wyrazie.\n\n")
            for i in range(number_verb):
                if list_verb[i] == letter:
                    antilist_verb[i] = letter
        
        else:
            print("Litera nie znajduję się w wyrazie. Zostaję ci odjęta jedna szansa.\n\n")
            lives -= 1

    print("Niestety straciłeś wszystkie szanse oraz przegrałeś grę.")
    while (True):
        answer2 = input("Czy chcesz zagrać jeszcze raz?(tak lub nie): ")
        if answer2 == "tak":
            break
        elif answer2 == "nie":
            exit()
        else:
            print("Podana odpowiedź jest nie prawidłowa.")
            continue
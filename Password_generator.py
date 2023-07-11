from random import choice

import os

start_loop = 0
while start_loop < 1:   # Create and start loop

    how_symbols = input('How many characters should the password contain?\n')   # Question to generate password
    start = input('You want create random password? (If yes push enter)\n')

    if start == '':   # Start generate password

        alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                    'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
                   '[', ']', '^', '_', '`', '{', '}', ']']

        alphabet_and_numbers = alphabet + numbers + symbols   # All library symbols possible in password

        generator = []

        how_symbols = int(how_symbols)

        for generate_password in range(how_symbols):
            generate = choice(alphabet_and_numbers)
            generator += generate

        convert_list = ''.join(generator)

        print(convert_list, '\n')   # Print ready password

        while True:   # Possibility again use generator
            use_again = input('You want use generator again? (yes or no)\n')
            if use_again == 'yes':
                os.system('cls')
                break
            elif use_again == 'no':
                exit()
            else:
                print('This is bad command, you write again.')

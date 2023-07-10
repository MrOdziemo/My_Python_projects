from random import randint

from time import sleep

import os

print('Hello in Found key game!\n'
      'Game area this coordinate system about of size x = 20 on y = 20. '
      'Your task is found value x and y on which is value key.\n')

print('Instruction to movement:\n'
      '- w (movement y value to up)\n'
      '- s (movement y value to down)\n'
      '- a (movement x value to down)\n'
      '- d (movement x value to up)\n')

game_position_key_x = randint(0, 20)  # Draw key position
game_position_key_y = randint(0, 20)

player_position_x = randint(0, 20)  # Draw player position
player_position_y = randint(0, 20)

start_loop = 0   # Create and start loop
while start_loop == 0:

    key_position = game_position_key_x, game_position_key_y  # Key position

    player_position = player_position_x, player_position_y  # Player position

    if key_position == player_position:   # When player found key
        print('Nice! You found key!\n'
              'This is you prize: https://www.youtube.com/watch?v=dQw4w9WgXcQ')  
        while True:
            end_game = input('You want play again? (yes or no)\n')
            if end_game == 'yes':
                print('Ok. Well play again.')
                sleep(2)
                os.system('cls')
                break
            elif end_game == 'no':
                print('Thank you for playing.')
                sleep(1)
                exit()
            else:
                print('Sorry, this is bad command.\n'
                      'You write again.\n')
                continue

    print('Your position x =', player_position_x, 'and y =', player_position_y, '\n')

    movement_player = input('Choose your move.\n')   # Computer asked to choose player

    match movement_player:   # Movement system
        case 'w' if player_position_y <= 19:  # Command on move to up
            player_position_y += 1
            os.system('cls')
        case 's' if player_position_y >= 1:  # Command on move to down
            player_position_y -= 1
            os.system('cls')
        case 'd' if player_position_x <= 19:   # Command on move to right
            player_position_x += 1
            os.system('cls')
        case 'a' if player_position_x >= 1:   # Command on move to left
            player_position_x -= 1
            os.system('cls')
        case _:   # Incorrect command move or movement is impossible
            print('Sorry, this is incorrect command or movement is impossible. You try again.')
            sleep(3.5)
            os.system('cls')

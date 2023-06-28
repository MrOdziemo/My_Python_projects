# Import time dictionary
import time
# Import os dictionary
import os
# import random dictionary
import random
# Program hello with player
print('Hello in the Tic Tac Too game!\n')
# Create variable to loop
play = 0
# Create loop the program
while play < 1:
    # Program give the question for player, how move want maked
    game = input('Choose your move\n'
                 '(paper, rock or scissors)\n')
    # Player choose your move
    if game == 'paper' or 'rock' or 'scissors':
        # Computer choose your move
        computer_move = random.choice(('paper', 'rock', 'scissors'))
        # Options to remis
        if game == computer_move:
            # Show move both players (realist player and computer player)
            print(f'Your move: {game}')
            print(f'Computer move: {computer_move}\n')
            print('Remis\n')
            while True:
                end_game = input('You want this play again?\n'
                                 '(Yes or No)\n')
                if end_game == 'Yes':
                    os.system('cls')
                    break
                elif end_game == "No":
                    print('Thank you for playing!')
                    time.sleep(2)
                    exit()
                else:
                    continue
        # Options to win for player and lose for computer
        elif (game == 'paper' and computer_move == 'rock') or (game == 'rock' and computer_move == 'scissors') or (
                game == 'scissors' and computer_move == 'paper'):
            # Show move both players (realist player and computer player)
            print(f'Your move: {game}')
            print(f'Computer move: {computer_move}\n')
            win_answer = random.choice(('You win! This great!',
                                        'Super! You win!',
                                        'Lucky game! Bravo!'))
            print(win_answer)
            print('')
            while True:
                end_game = input('You want this play again?\n'
                                 '(Yes or No)\n')
                if end_game == 'Yes':
                    os.system('cls')
                    break
                elif end_game == "No":
                    print('Thank you for playing!')
                    time.sleep(2)
                    exit()
                else:
                    continue
        # Options to win for computer and lose for player
        elif (game == 'rock' and computer_move == 'paper') or (game == 'scissors' and computer_move == 'rock') or (
                game == 'paper' and computer_move == 'scissors'):
            # Show move both players (realist player and computer player)
            print(f'Your move: {game}')
            print(f'Computer move: {computer_move}\n')
            lose_answer = random.choice(('Unfortunately. You lose this time',
                                         "Oh no! You lose. You'll do better next time",
                                         'You lose... well you were unlucky'))
            print(lose_answer)
            print('')
            while True:
                end_game = input('You want this play again?\n'
                                 '(Yes or No)\n')
                if end_game == 'Yes':
                    os.system('cls')
                    break
                elif end_game == "No":
                    print('Thank you for playing!')
                    time.sleep(2)
                    exit()
                else:
                    continue
        # Choose bad move by player
        elif game != 'paper' or 'rock' or 'scissors':
            # Show move player
            print(f'Your move {game}\n')
            print("Bad change. Don't have this option dude\n")
            while True:
                end_game = input('You want this play again?\n'
                                 '(Yes or No)\n')
                if end_game == 'Yes':
                    os.system('cls')
                    break
                elif end_game == "No":
                    print('Thank you for playing!')
                    time.sleep(2)
                    exit()
                else:
                    continue
        else:
            continue
    else:
        continue

import time
# import dictionary
import os

print('Hello in PESEL converter\n')  # Computer welcome user

start_loop = 0
# Create loop
while start_loop < 1:

    pesel = input('Write your pesel number:\n')  # Computer asks to write user pesel

    second_part_year = (pesel[0:2])
    day = (pesel[4:6])  # Download data to create date of birth
    month = (pesel[2:4])

    if second_part_year == "02":  # Option when user born after 2000 year
        year = 20
        total_month = int(month) - 20
        data = day + '.' + str(total_month) + '.' + str(year) + second_part_year
        print(data)
        while True:
            end = input('\nYou want converter again?(yes or no)')
            if end == 'yes':
                os.system('cls')
                break
            elif end == 'no':
                print('Thank you for using converter')
                time.sleep(2)
                exit()

    elif int(second_part_year) >= 10 <= 99:  # Option when user born before 2000 year
        year = 19
        data = day + '.' + str(month) + '.' + str(year) + second_part_year
        print(data)
        while True:
            end = input('\nYou want converter again?(yes or no)')
            if end == 'yes':
                os.system('cls')
                break
            elif end == 'no':
                print('Thank you for using converter')
                time.sleep(2)
                exit()

    else:  # Option when user written bad pesel
        print('Bad written pesel.\n'
              'You write again.\n')
        time.sleep(2)
        os.system('cls')
        break

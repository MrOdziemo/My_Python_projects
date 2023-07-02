# import dt library
import time

import os

import aspose.pdf as ap

# welcome to program
print('Hello in test on Asperger Syndrome.\n'
      'This test show you, do you have Asperger Syndrome.\n'
      "The test consists of 50 questions.\n\n"
      "It covers social skills, the ability to shift attention easily, "
      "attention to detail, communication and imagination.\n"
      "For each question, 1 point is awarded when the answer indicates the presence of autistic features.\n"
      "The questions were formulated in such a way that half of the answers were affirmative and half were negative.\n"
      "\nThe test is to help determine the level of autism traces in normal people.\n"
      "Even a high score does not mean that the person suffers from an autistic-type disorder.\n"
      "However, when the result exceeds 32, it is recommended to consult a specialist.\n")
# Start loop with questions
start_loop = 0
while start_loop < 1:
    # User have a choice do want to make a test
    start_test = input('Do you ready on make a test?\n'
                       '(yes or no)\n')
    # Choice one if user want to make a test
    if start_test == 'yes':
        # Create punctuation
        test_score = 0
        # Asking questions
        while True:
            print('\nQuestion 1')
            question_one = input('I prefer to do things in a group than alone.\n')
            if question_one == 'true':
                break
            elif question_one == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 2')
            question_two = input('I prefer to do things the same way all the time.\n')
            if question_two == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 3')
            question_three = input("If I'm trying to imagine something, "
                                   "I have no problem forming that image in my mind.\n")
            if question_three == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 4')
            question_four = input("I'm often so absorbed in one thing that I don't notice anything else.\n")
            if question_two == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 5')
            question_five = input('I often hear small noises that others cannot hear.\n')
            if question_five == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 6')
            question_six = input('I often remember bits and pieces of information, such as car registration numbers.\n')
            if question_six == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 7')
            question_seven = input('It often happens to me that people point out to me that what I said was rude, '
                                   'although I have the impression that it was polite.\n')
            if question_seven == 'true':
                test_score += 1
                break
            elif question_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 8')
            question_eight = input('When I read a book, I can easily imagine what the characters look like.\n')
            if question_eight == 'true':
                break
            elif question_eight == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 9')
            question_nine = input('I am fascinated by dates.\n')
            if question_nine == 'true':
                test_score += 1
                break
            elif question_nine == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 10')
            question_ten = input('I have no trouble understanding what is being said, '
                                 'even if several people are discussing it at the same time.\n')
            if question_ten == 'true':
                break
            elif question_ten == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 11')
            question_eleven = input('Social meetings are not a problem for me.\n')
            if question_eleven == 'true':
                break
            elif question_eleven == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 12')
            question_twelve = input('I notice details that are not visible to others.\n')
            if question_twelve == 'true':
                test_score += 1
                break
            elif question_twelve == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 13')
            question_thirteen = input("I'd rather go to the library than to a party.\n")
            if question_thirteen == 'true':
                test_score += 1
                break
            elif question_thirteen == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 14')
            question_fourteen = input('I have no problem making up stories.\n')
            if question_fourteen == 'true':
                break
            elif question_fourteen == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 15')
            question_fifteen = input('I am more attached to people than to things.\n')
            if question_fifteen == 'true':
                break
            elif question_fifteen == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 16')
            question_sixteen = input("When I'm dealing with a problem, "
                                     "I get nervous when I have to stop what "
                                     "I'm doing and I can't continue what I'm doing.\n")
            if question_sixteen == 'true':
                test_score += 1
                break
            elif question_sixteen == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 17')
            question_seventeen = input('I like chatting about nothing, e.g. in the elevator.\n')
            if question_seventeen == 'true':
                break
            elif question_seventeen == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 18')
            question_eighteen = input('When I say something, I often do not allow others to speak.\n')
            if question_eighteen == 'true':
                test_score += 1
                break
            elif question_eighteen == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 19')
            question_nineteen = input('I am fascinated by numbers.\n')
            if question_nineteen == 'true':
                test_score += 1
                break
            elif question_nineteen == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 20')
            question_twenty = input('When I read a book, I have trouble imagining what the characters look like.\n')
            if question_twenty == 'true':
                test_score += 1
                break
            elif question_twenty == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 21')
            question_twenty_one = input("I don't enjoy reading fiction.\n")
            if question_twenty_one == 'true':
                test_score += 1
                break
            elif question_twenty_one == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 22')
            question_twenty_two = input('I have trouble making friends.\n')
            if question_twenty_two == 'true':
                test_score += 1
                break
            elif question_twenty_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 23')
            question_twenty_three = input('Very often I notice that things are arranged according to patterns, '
                                          'template.\n')
            if question_twenty_three == 'true':
                test_score += 1
                break
            elif question_twenty_three == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 24')
            question_twenty_four = input("I'd rather go to the theater than to the museum.\n")
            if question_twenty_four == 'true':
                break
            elif question_twenty_four == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 25')
            question_twenty_five = input("It doesn't bother me at all when my daily rhythm is somehow disturbed.\n")
            if question_twenty_five == 'true':
                break
            elif question_twenty_five == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 26')
            question_twenty_six = input('I often find myself not knowing how to keep the conversation going.\n')
            if question_twenty_six == 'true':
                test_score += 1
                break
            elif question_twenty_six == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 27')
            question_twenty_seven = input(
                "I have no problems 'reading between the lines' when someone is talking to me.\n")
            if question_twenty_seven == 'true':
                break
            elif question_twenty_seven == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 28')
            question_twenty_eight = input('I focus more on the whole than on the details.\n')
            if question_twenty_eight == 'true':
                break
            elif question_twenty_eight == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 29')
            question_twenty_nine = input('I have trouble remembering phone numbers.\n')
            if question_twenty_nine == 'true':
                break
            elif question_twenty_nine == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 30')
            question_thirty = input("I usually don't notice minor changes in people's position or appearance.\n")
            if question_thirty == 'true':
                break
            elif question_thirty == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 31')
            question_thirty_one = input('I notice when what I say starts to bore others.\n')
            if question_thirty_one == 'true':
                break
            elif question_thirty_one == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 32')
            question_thirty_two = input('I have no problem doing more than one task at a time.\n')
            if question_thirty_two == 'true':
                break
            elif question_thirty_two == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 33')
            question_thirty_three = input("When I'm on the phone, I don't know whose turn it is.\n")
            if question_thirty_three == 'true':
                test_score += 1
                break
            elif question_thirty_three == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 34')
            question_thirty_four = input('I like to do many things at the same time.\n')
            if question_thirty_four == 'true':
                break
            elif question_thirty_four == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 35')
            question_thirty_five = input('I am often the last person to understand a joke.\n')
            if question_thirty_five == 'true':
                test_score += 1
                break
            elif question_thirty_five == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 36')
            question_thirty_six = input(
                'I have no problem guessing what someone is feeling or thinking from their facial expressions.\n')
            if question_thirty_six == 'true':
                break
            elif question_thirty_six == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 37')
            question_thirty_seven = input(
                "If I have to stop what I'm doing, I have no problem getting back to it immediately.\n")
            if question_thirty_seven == 'true':
                break
            elif question_thirty_seven == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 38')
            question_thirty_eight = input('I can talk about anything.\n')
            if question_thirty_eight == 'true':
                break
            elif question_thirty_eight == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 39')
            question_thirty_nine = input('People point out to me that I talk about the same thing all the time.\n')
            if question_thirty_nine == 'true':
                test_score += 1
                break
            elif question_thirty_nine == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 40')
            question_forty = input('When I was a kid, I liked to play dress-up and pretend I was someone else.\n')
            if question_forty == 'true':
                break
            elif question_forty == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 41')
            question_forty_one = input(
                'I like to collect information on different categories of items (brands of cars, species of birds)\n')
            if question_forty_one == 'true':
                test_score += 1
                break
            elif question_forty_one == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 42')
            question_forty_two = input('I have trouble imagining what it would be like to be someone else.\n')
            if question_forty_two == 'true':
                test_score += 1
                break
            elif question_forty_two == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 43')
            question_forty_three = input('I like when every activity I participate in is carefully planned.\n')
            if question_forty_three == 'true':
                test_score += 1
                break
            elif question_forty_three == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 44')
            question_forty_four = input('I like socializing.\n')
            if question_forty_four == 'true':
                break
            elif question_forty_four == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 45')
            question_forty_five = input('Recognizing human emotions is difficult for me.\n')
            if question_forty_five == 'true':
                test_score += 1
                break
            elif question_forty_five == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 46')
            question_forty_six = input('I am nervous in new situations.\n')
            if question_forty_six == 'true':
                test_score += 1
                break
            elif question_forty_six == 'false':
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 47')
            question_forty_seven = input('I like meeting new people.\n')
            if question_forty_seven == 'true':
                break
            elif question_forty_seven == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 48')
            question_forty_eight = input("I'm a good diplomat.\n")
            if question_forty_eight == 'true':
                break
            elif question_forty_eight == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 49')
            question_forty_nine = input('Remembering birthdays is a problem for me.\n')
            if question_forty_nine == 'true':
                break
            elif question_forty_nine == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                continue

        while True:
            print('\nQuestion 50')
            question_fifty = input(
                'Playing games with children where I have to pretend something or someone is easy for me.\n')
            if question_fifty == 'true':
                break
            elif question_fifty == 'false':
                test_score += 1
                break
            else:
                print("I'm sorry. You write incorrect commend.\n"
                      "You write again")
                continue
        # Counting questions
        print('\nGreat! End of test.\n'
              'You answers:\n'
              f'Question 1: {question_one}\n'
              f'Question 2: {question_two}\n'
              f'Question 3: {question_three}\n'
              f'Question 4: {question_four}\n'
              f'Question 5: {question_five}\n'
              f'Question 6: {question_six}\n'
              f'Question 7: {question_seven}\n'
              f'Question 8: {question_eight}\n'
              f'Question 9: {question_nine}\n'
              f'Question 10: {question_ten}\n'
              f'Question 11: {question_eleven}\n'
              f'Question 12: {question_twelve}\n'
              f'Question 13: {question_thirteen}\n'
              f'Question 14: {question_fourteen}\n'
              f'Question 15: {question_fifteen}\n'
              f'Question 16: {question_sixteen}\n'
              f'Question 17: {question_seventeen}\n'
              f'Question 18: {question_eighteen}\n'
              f'Question 19: {question_nineteen}\n'
              f'Question 20: {question_twenty}\n'
              f'Question 21: {question_twenty_one}\n'
              f'Question 22: {question_twenty_two}\n'
              f'Question 23: {question_twenty_three}\n'
              f'Question 24: {question_twenty_four}\n'
              f'Question 25: {question_twenty_five}\n'
              f'Question 26: {question_twenty_six}\n'
              f'Question 27: {question_twenty_seven}\n'
              f'Question 28: {question_twenty_eight}\n'
              f'Question 29: {question_twenty_nine}\n'
              f'Question 30: {question_thirty}\n'
              f'Question 31: {question_thirty_one}\n'
              f'Question 32: {question_thirty_two}\n'
              f'Question 33: {question_thirty_three}\n'
              f'Question 34: {question_thirty_four}\n'
              f'Question 35: {question_thirty_five}\n'
              f'Question 36: {question_thirty_six}\n'
              f'Question 37: {question_thirty_seven}\n'
              f'Question 38: {question_thirty_eight}\n'
              f'Question 39: {question_thirty_nine}\n'
              f'Question 40: {question_forty}\n'
              f'Question 41: {question_forty_one}\n'
              f'Question 42: {question_forty_two}\n'
              f'Question 43: {question_forty_three}\n'
              f'Question 44: {question_forty_four}\n'
              f'Question 45: {question_forty_five}\n'
              f'Question 46: {question_forty_six}\n'
              f'Question 47: {question_forty_seven}\n'
              f'Question 48: {question_forty_eight}\n'
              f'Question 49: {question_forty_nine}\n'
              f'Question 50: {question_fifty}\n')
        # Show number points
        print(f'Your result in test to {test_score} points.\n')
        # Option one if cross 32 points
        if test_score > 32:
            print("You've crossed the cut-off point. However, "
                  "remember that this is only a screening test. "
                  "This does not yet mean that you have an autism spectrum disorder, "
                  "but it gives grounds for consulting a specialist in this area.")
            end_program = input('You want exit program? (yes or no)\n')
            if end_program == 'yes':
                while True:
                    report_create = input('Whether create file pdf with answers in aq test? (yes or no)\n')
                    if report_create == 'yes':
                        # Create pdf file
                        document = ap.Document()
                        page = document.pages.add()
                        text = ap.text.TextFragment("                       Summary AQ test\n\n"
                                                    "This is answers made of AQ test:\n\n"
                                                    "'You answers:\n"
                                                    f'Question 1: {question_one}\n'
                                                    f'Question 2: {question_two}\n'
                                                    f'Question 3: {question_three}\n'
                                                    f'Question 4: {question_four}\n'
                                                    f'Question 5: {question_five}\n'
                                                    f'Question 6: {question_six}\n'
                                                    f'Question 7: {question_seven}\n'
                                                    f'Question 8: {question_eight}\n'
                                                    f'Question 9: {question_nine}\n'
                                                    f'Question 10: {question_ten}\n'
                                                    f'Question 11: {question_eleven}\n'
                                                    f'Question 12: {question_twelve}\n'
                                                    f'Question 13: {question_thirteen}\n'
                                                    f'Question 14: {question_fourteen}\n'
                                                    f'Question 15: {question_fifteen}\n'
                                                    f'Question 16: {question_sixteen}\n'
                                                    f'Question 17: {question_seventeen}\n'
                                                    f'Question 18: {question_eighteen}\n'
                                                    f'Question 19: {question_nineteen}\n'
                                                    f'Question 20: {question_twenty}\n'
                                                    f'Question 21: {question_twenty_one}\n'
                                                    f'Question 22: {question_twenty_two}\n'
                                                    f'Question 23: {question_twenty_three}\n'
                                                    f'Question 24: {question_twenty_four}\n'
                                                    f'Question 25: {question_twenty_five}\n'
                                                    f'Question 26: {question_twenty_six}\n'
                                                    f'Question 27: {question_twenty_seven}\n'
                                                    f'Question 28: {question_twenty_eight}\n'
                                                    f'Question 29: {question_twenty_nine}\n'
                                                    f'Question 30: {question_thirty}\n'
                                                    f'Question 31: {question_thirty_one}\n'
                                                    f'Question 32: {question_thirty_two}\n'
                                                    f'Question 33: {question_thirty_three}\n'
                                                    f'Question 34: {question_thirty_four}\n'
                                                    f'Question 35: {question_thirty_five}\n'
                                                    f'Question 36: {question_thirty_six}\n'
                                                    f'Question 37: {question_thirty_seven}\n'
                                                    f'Question 38: {question_thirty_eight}\n'
                                                    f'Question 39: {question_thirty_nine}\n'
                                                    f'Question 40: {question_forty}\n'
                                                    f'Question 41: {question_forty_one}\n'
                                                    f'Question 42: {question_forty_two}\n'
                                                    f'Question 43: {question_forty_three}\n'
                                                    f'Question 44: {question_forty_four}\n'
                                                    f'Question 45: {question_forty_five}\n'
                                                    f'Question 46: {question_forty_six}\n'
                                                    f'Question 47: {question_forty_seven}\n'
                                                    f'Question 48: {question_forty_eight}\n'
                                                    f'Question 49: {question_forty_nine}\n'
                                                    f'Question 50: {question_fifty}\n\n'
                                                    f'Your number points: {test_score}\n\n'
                                                    "You've crossed the cut-off point. "
                                                    "However, remember that this is only a screening test. "
                                                    "This does not yet mean that you have an autism spectrum disorder, "
                                                    "but it does give grounds for consulting a specialist in this area. "
                                                    "Save the result in pdf to avoid re-filling. "
                                                    "The printout will support the initial consultation. "
                                                    "If you are unsure, "
                                                    "you can ask a loved one to take the test for you and talk about any differences in your results.")
                        page.paragraphs.add(text)
                        document.save('Summary Document AQ test.pdf')
                        print("Created file:\n"
                              "'Summary Document AQ test.pdf'\n")
                        print('Thank you for using AQ Test :)')
                        time.sleep(3)
                        exit()
                    elif report_create == 'no':
                        print('Thank you for using AQ test :)')
                        time.sleep(3)
                        exit()
                    else:
                        continue
            elif end_program == 'no':
                print('Test will make again.')
                time.sleep(2)
                os.system('cls')
                break
            else:
                continue
        # Option one if not cross 32 points
        elif test_score <= 32:
            print("You didn't exceed point threshold. You don't show autistic behaviour.\n"
                  "You don't need call to the specialist :)")
            end_program = input('You want exit program? (yes or no)\n')
            if end_program == 'yes':
                print('Thank you for using AQ test :)')
                time.sleep(3)
                exit()
            elif end_program == 'no':
                print('Test will make again.')
                time.sleep(2)
                os.system('cls')
                break
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                time.sleep(3)
                continue
        else:
            pass
    # Choice one if user want to make a test
    elif start_test == 'no':
        print('You need more time?\n'
              'No problem! I give you several seconds.\n')
        time.sleep(5)
        while True:
            print('Well, You want try make a test?\n'
                  "If yes write 'yes', if no  write 'no'")
            again_start = input()
            if again_start == 'yes':
                print('Alright! So we tried again.\n')
                os.system('cls')
                break
            elif again_start == 'no':
                print('\nUnderstand. Thank you that you tried.\n'
                      'See you later!')
                time.sleep(5)
                exit()
            else:
                print("I'm sorry. You write incorrect command.\n"
                      "You write again")
                time.sleep(3)
                continue
    # Option when user write incorrect command
    else:
        print("I'm sorry. You write incorrect command.\n"
              "You write again.\n\n")
        time.sleep(1)
        continue

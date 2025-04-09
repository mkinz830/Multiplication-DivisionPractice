import random
from os import system
system('mode con cols=70 lines=20')

def begin(message=''):
    system('cls')
    print(message)
    print(' Multiplication and Division Practice!')
    print('')
    number_of_choice = input(' Which number would you like to practice?: ')
    try:
        number_of_choice = int(number_of_choice)
    except:
        return begin("\n You didn't enter a number! Try again.\n")
    correct, incorrect = practice(number_of_choice)
    return correct, incorrect

def practice(number_of_choice):        
    system('cls')
    list_of_twelve = list(range(0,13))
    correct = 0
    incorrect = 0
    div_or_mult = input(' Would you like to practice multiplication (m) or division (d)?: ')
    if div_or_mult not in ['d', 'm']:
        input(' Did not enter correct option, press enter to try again. ')
        return practice(number_of_choice)
    while list_of_twelve:
        index_to_pop = random.randrange(len(list_of_twelve))
        number_to_use = list_of_twelve.pop(index_to_pop)
        if div_or_mult == 'm':
            new_correct,new_incorrect = multiply_by(number_of_choice, number_to_use)
            correct += new_correct
            incorrect += new_incorrect
        else:
            new_correct,new_incorrect = divide_by(number_of_choice, number_to_use)
            correct += new_correct
            incorrect += new_incorrect
    return correct, incorrect

def multiply_by(number_of_choice, number_to_multiply_by):
    system('cls')
    print('')
    correct = 0
    incorrect = 0
    product = number_of_choice * number_to_multiply_by
    string_to_show = ' ' + str(number_of_choice) + ' × ' + str(number_to_multiply_by) + ' = '
    answer = int(input(string_to_show))
    if product == answer:
        correct += 1
        print(' CONGRATULATIONS! YOU GOT IT RIGHT! ')
        input(' Press ENTER to go to next equation. ')
    else:
        incorrect += 1
        print(' Sorry, that answer is incorrect.')
        input(' Press ENTER to try again.')        
        new_correct, new_incorrect = multiply_by(number_of_choice, number_to_multiply_by)
        correct += new_correct
        incorrect += new_incorrect
    return correct, incorrect

def divide_by(number_of_choice, number_to_divide_with):
    system('cls')
    print('')
    correct = 0
    incorrect = 0
    first_number = number_of_choice * number_to_divide_with
    string_to_show = ' ' + str(first_number) + ' ÷ ' + str(number_of_choice) + ' = '
    answer = int(input(string_to_show))
    if number_to_divide_with == answer:
        correct += 1
        print(' CONGRATULATIONS Jordyn! YOU GOT IT RIGHT! ')
        input(' Press ENTER to go to next equation. ')
    else:
        incorrect += 1
        print(' Sorry, that answer is incorrect.')
        input(' Press ENTER to try again.')        
        new_correct, new_incorrect = divide_by(number_of_choice, number_to_divide_with)
        correct += new_correct
        incorrect += new_incorrect
    return correct, incorrect

while True:
    correct, incorrect = begin()
    system('cls')
    print('')
    print(' You got ', correct, ' correct answers')
    print(' You got ', incorrect, ' incorrect answers')
    percent_correct = round(100*(correct/(correct+incorrect)), 2)
    print(' Total percent: ', percent_correct)
    if percent_correct >= 85:
        print(' AMAZING JOB Jordyn! Keep up the good work!')
    else:
        print(" GREAT TRY! You're almost there! ")
    input(' Hit enter to pick another number to practice.')
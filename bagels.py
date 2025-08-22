import random
import string
import os

def Guess(random_number, guess):

    if random_number == guess:
        print('You got it!\n'
              'Would you like to play again? (yes or no)')
        print('> ', end='')

        if input() == 'yes':
            print('\n')
            os.system('clear')
            StartGame()
        else:
            os.system('clear')
            exit(0)


    for i in range(len(guess)):
        if guess[i] == random_number[i]:
            print('Fermi')
        elif guess[i] in random_number:
            print('Pico')
        else:
            print('Bagels')
    
                

def GameLoop():
    guessCounter = 1
    length = 3

    random_number = ''.join(random.choices(string.digits, k=length)) # creates random number

    #print(random_number) # The Answer

    while True:
        print(f'Guess #{guessCounter}:')
        print('> ', end="")
        guess = input() 
        guessCounter += 1
        
        if guessCounter < 11:
            Guess(random_number, guess)

        elif guessCounter > 10:
            print('You ran out of guesses.')
            print(f'The correct answer was {random_number}')
            print('Would you like to try again?')
            print('> ', end='')

            if input() == 'yes':
                print('\n')
                os.system('clear')
                StartGame()
            else:
                os.system('clear')
                exit(0)




def StartGame():

    print('Bagels, a deductive logic game.\n'
          'By Juan Cota jcota@gmail.com\n'
          'I am thinking of a 3-digit number. Try to guess what it is.\n'
          'Here are some clues:\n'
          'When I say:    That means:\n'
          '  Pico         One digit is correct but in the wrong position.\n'
          '  Fermi        One digit is correct and in the right position.\n'
          '  Bagels       No digit is correct.\n'
          'I have thought up a number.\n'
          ' You have 10 guesses to get it.')

    GameLoop()
            

if __name__ == '__main__':
    os.system('clear')
    StartGame()    

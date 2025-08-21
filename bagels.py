import random
import string

def Guess(random_number, guess):
    iguess = 0
    jguess = 0

    if random_number == guess:
        print('You got it!')
        

    for i in random_number:
        for j in guess:
            if i == j:
                if iguess == jguess:
                    print('Fermi')
                elif i == j:
                    print('Pico')
                else: print('Bagels')
                
                iguess += 1

                if iguess == 2:
                    iguess = 0
                    jguess += 1
                

def GameLoop():
    guessCounter = 1
    length = 3

    random_number = ''.join(random.choices(string.digits, k=length)) # creates random number
    print(f'Guess #{guessCounter}:')
    print(random_number)

    while True:
        print('> ', end="")
        guess = input() 
        Guess(random_number, guess)



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
    StartGame()    

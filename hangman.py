import random
import string
from wordsList import words

def getValidWord (words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word


def hangman ():
    word = getValidWord(words)
    wordLetters = set(word) #  separates letters of word
    alphabet = set (string.ascii_uppercase)
    usedLetters = set()  # empty set to store letter

    lives = 3

    while len(wordLetters) > 0 and lives > 0:

        # ' '.join(['a, 'b' ,'cd']) --> 'a b cd'

        print(f'u hv {lives} lives left and used these letters :' , ' '.join(usedLetters))

        #what current word is ( ie W - R D)
        word_list = [letter if letter in usedLetters else '-' for letter in word]
        
        print ('current word :' , ' '.join(word_list))

        userLetter = input(' guess letter : ').upper()
       
        if userLetter in alphabet - usedLetters: #hyphen used in finding sequence of words
            usedLetters.add(userLetter)

            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

            else:
                lives = lives-1
                print('letter is not in word')

        elif userLetter in usedLetters:
            print('already used')

        else :
            print('invalid character')
    if lives == 0:
        print('u lost, word was....', word)
    else:
        print('u gesses right...', word)


hangman()
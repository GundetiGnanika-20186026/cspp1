'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


#########################################################
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str_ing = "abcdefghijklmnopqrstuvwxyz"
    li_st = list(str_ing)
    for i in letters_guessed:
        if i in li_st:
            li_st.remove(i)
    return ''.join(li_st)
##############################################################
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    str_ing = ""
    for char in secret_word:
        if char in letters_guessed:
            str_ing = str_ing + char
        else:
            str_ing = str_ing + "_"
    return str_ing
#########################################################
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    len_secret_word = len(secret_word)
    cou_nt = 0
    for char in secret_word:
        if char in letters_guessed:
            cou_nt = cou_nt + 1
    if cou_nt == len_secret_word:
        return "True"
    return "False"


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    guess_left = 8
    letters_guessed = ''
    while guess_left != 0:
        print(" You have " + str(guess_left) +" guesses left")
        print("available letters are: "+get_available_letters(letters_guessed))
        char = input("guess a letter: ")
        if char in secret_word and char not in letters_guessed:
            letters_guessed += char
            print("correct guess: "+get_guessed_word(secret_word, letters_guessed))

        elif char in letters_guessed:
            print("the guess is already selected"+get_guessed_word(secret_word, letters_guessed))
            
        else:
            letters_guessed += char
            print("the guess is wrong "+get_guessed_word(secret_word, letters_guessed))
            guess_left =guess_left - 1

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            return ("you won !!"+get_guessed_word(secret_word, letters_guessed))
        if guess_left <= 0:
           print("you lost the game!!")
           break


def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = chooseWord(wordlist).lower()
    print(hangman(secret_word))
    
if __name__ == "__main__":
    main()

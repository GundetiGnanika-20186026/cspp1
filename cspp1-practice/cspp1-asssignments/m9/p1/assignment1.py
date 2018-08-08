'''
Author:Gnanika
Date: 8 August 2018
'''
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
def main():
    '''
    Main function for the program
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()

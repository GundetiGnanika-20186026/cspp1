'''
Author:Gnanika
Date: 9 August 2018
'''
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
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()

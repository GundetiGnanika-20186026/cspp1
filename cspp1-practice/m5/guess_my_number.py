'''
Auther:Gnanika
Date:3 August 2018
'''

def main():
    '''guessing number'''
    lo_w = 0
    h_i = 100
    print("please think of a number between 0 and 100")
    print("Enter 'h' to indicate the guess is too high")
    print("Enter 'l' to indicate the guess is too low")
    print("Enter 'c' to indicate I guessed correctly")
    print("is your secret number 50?")
    m_i = (lo_w + h_i)//2
    print(m_i)
    i = input()
    while m_i <= 100:
        if i == 'h':
            h_i = m_i
            m_i = (lo_w+h_i)//2
            print("is your secret number "+str(m_i)+"?")
            i = input()
        elif i == 'l':
            lo_w = m_i
            m_i = (lo_w+h_i)//2
            print("is your secret number "+str(m_i)+"?")
            i = input()
        elif i == 'c':
            print("Game Over. I successfully guessed your secret number")
            break
        else:
            print("sorry,I did not understand your input")
            print("Enter 'h' to indicate the guess is too high")
            print("Enter 'l' to indicate the guess is too low")
            print("Enter 'c' to indicate I guessed correctly")
            i = input()
if __name__ == "__main__":
    main()

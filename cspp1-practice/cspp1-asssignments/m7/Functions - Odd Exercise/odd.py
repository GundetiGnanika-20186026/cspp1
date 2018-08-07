'''
Author:Gnanika
Date:6 August
'''


def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return x % 2 != 0
    

def main():
    '''finding weather a number is odd'''
    data = input()
    print(odd(int(data)))

if __name__== "__main__":
    main()

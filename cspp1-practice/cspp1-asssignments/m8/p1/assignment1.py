'''
Author:Gnanika
Date:7 August 2018
'''
def factorial(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num in (1, 0):
        return 1
    return num * factorial(num - 1)
def main():
    '''main function'''
    a_in = input()
    print(factorial(int(a_in)))
if __name__ == "__main__":
    main()

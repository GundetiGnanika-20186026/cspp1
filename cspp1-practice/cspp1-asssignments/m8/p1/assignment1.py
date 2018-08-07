'''
Author:Gnanika
Date:7 August 2018
'''
def factorial(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)
def main():
    '''main function'''
    a = input()
    print(factorial(int(a)))    

if __name__ == "__main__":
    main()

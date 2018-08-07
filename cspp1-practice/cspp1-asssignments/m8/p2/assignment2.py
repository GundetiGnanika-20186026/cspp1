'''
Author:Gnanika
Date:7 August 2018
'''
def sumofdigits(num):
    '''
    num is positive Integer
    returns: a positive integer, the sum of digits of num.
    '''
    if num == 0:
        return num
    return (num % 10 + sumofdigits(num//10))
def main():
    '''main function'''
    a = input()
    print(sumofdigits(int(a)))
if __name__ == "__main__":
    main()

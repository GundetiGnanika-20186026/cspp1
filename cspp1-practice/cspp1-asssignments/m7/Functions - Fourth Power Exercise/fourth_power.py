'''
Author:Gnanika
date: 6 August 2018
'''
def square(x_v):
    '''
    x: int or float.
    '''
    return x_v ** 2
def fourthpower(x_v):
    '''
    x: int or float.
    '''
    return square(square(x_v))
def main():
    '''finding the fourth power of given number '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourthpower(int(float(str(data)))))
    else:
        print(fourthpower(data))
if __name__ == "__main__":
    main()

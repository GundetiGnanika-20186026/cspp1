'''
Author :Gnanika
Date: 7 August 2018
'''
def recurpower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recurpower(base, exp - 1)
def main():
    '''main function '''
    data = input()
    data = data.split()
    print(recurpower(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()

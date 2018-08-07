'''
Author:Gnanika
Date:7 August 2018
'''
def iterpower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    output = 1
    while exp > 0:
        output = output * base
        exp = exp - 1
    return output
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(iterpower(float(data[0]), int(data[1])))
if __name__ == "__main__":
    main()

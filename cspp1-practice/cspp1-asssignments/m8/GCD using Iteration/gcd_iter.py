'''
Author:Gnanika
Date:7 August 2018
'''
def gcditer(a_in, b_in):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = 0
    min_value = min(a_in, b_in)
    for i in range(min_value, 0, -1):
        if a_in % i == 0 and b_in % i == 0:
            break
    return i
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()

'''
Author:Gnanika
Date: 7 August 2018
'''
def gcdrecur(a_in, b_in):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b_in > a_in:
        a_in, b_in = b_in, a_in
    if b_in % a_in == 0:
        return a_in
    return gcdrecur(b_in, (a_in % b_in))
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()

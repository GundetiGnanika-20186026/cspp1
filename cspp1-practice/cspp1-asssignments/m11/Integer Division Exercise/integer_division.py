'''
Author :Gnanika
Date: 10 August 2018
'''
def integer_division(xnum, anum):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while xnum >= anum:
        count += 1
        xnum = xnum - anum
    return count
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
    
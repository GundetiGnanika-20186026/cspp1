'''
Author:Gnanika
Date: 4 August 2018

'''
def main():
    '''
    calculating the products of integers in the given number
    '''
    int_input = int(input())
    product = 1
    while int_input > 0:
        reminde_r = int_input % 10
        product = product * reminde_r
        int_input = int_input // 10
    print(product)
if __name__ == "__main__":
    main()

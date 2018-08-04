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
    extra = int_input
    while int_input > 0:
        reminde_r = int_input % 10
        product = product * reminde_r
        int_input = int_input // 10
    if extra > 0:
        print(str(product))
    while int_input < 0:
        int_input = -(int_input)
        reminde_r = int_input % 10
        product = product * reminde_r
        int_input = int_input // 10
        int_input = -(int_input)
    if extra < 0:
        print("-"+ str(product))
    
if __name__ == "__main__":
    main()

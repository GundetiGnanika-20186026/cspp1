'''
Author:Gnanika
Date: 4 August 2018

'''
def main():
    '''
    calculating the sum of integers in the given number
    '''
    int_input = int(input())
    su_m = 0
    while int_input > 0:
        reminde_r = int_input % 10
        su_m = su_m + reminde_r
        int_input = int_input // 10
    print(su_m)
if __name__ == "__main__":
    main()

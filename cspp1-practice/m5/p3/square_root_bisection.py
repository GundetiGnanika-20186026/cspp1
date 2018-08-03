'''
Author:Gnanika
Date:3 August 2018
'''

def main():
    '''square using bisection method '''
    num = int(input())
    epsilon = 0.01
    #step = 0.1
    n_guess = 0
    lo_w = 0
    hi_gh = num
    midd_le = (hi_gh + lo_w) / 2
    while abs(midd_le ** 2 - num) >= epsilon:
        n_guess += 1
        if midd_le ** 2 < num:
            lo_w = midd_le
        else:
            hi_gh = midd_le
        midd_le = (hi_gh + lo_w) / 2.0
    print(str(midd_le))

if __name__ == "__main__":
    main()

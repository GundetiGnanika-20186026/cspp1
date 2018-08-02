'''
Author:Gnanika
Date:2 August 2018
'''

def main():
    ''' printing the number of vowels'''
    s_t = input()
    n_v = 0
    for ch_ar in s_t:
        if ch_ar in ('a', 'e', 'i', 'o', 'u'):
            n_v += 1
    print("Number of vowels:"+" "+str(n_v))

if __name__ == "__main__":
    main()

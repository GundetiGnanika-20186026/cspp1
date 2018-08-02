'''
Author:Gnanika
Date:2 August 2018
'''

def main():
    S_T = input()
    N_V = 0
    for ch_ar in S_T:
        if ch_ar == 'a' or ch_ar == 'e' or ch_ar == 'i' or ch_ar == 'o' or ch_ar == 'u':
             N_V += 1
    print("Number of vowels:"+" "+str(N_V))

if __name__ == "__main__":
	main()

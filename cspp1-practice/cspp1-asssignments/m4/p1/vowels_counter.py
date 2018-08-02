'''
Author:Gnanika
Date:2 August 2018
'''

def main():
	S_T = input()
	N_V = 0
	for char in S_T:
		if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
			N_V += 1
	print("Number of vowels:"+" "+str(N_V))

if __name__== "__main__":
	main()

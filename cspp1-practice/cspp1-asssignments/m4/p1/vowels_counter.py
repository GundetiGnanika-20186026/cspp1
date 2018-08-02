#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	S_t = input("enter the string:")
	# the input string is in s
	# remove pass and start your code here
	N_V = 0 
	for char in s_t :
		if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
			N_V += 1

	print ("Number of Vowels:" + str(N_V)) 


	



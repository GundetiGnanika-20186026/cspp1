'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str2 = ''
    for i in string:
    	if ('a'<= i >= 'z') or ('A' <= i >= 'Z') or ('0' <= i >= '9'):
    		str2 += i
    
    return str2

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

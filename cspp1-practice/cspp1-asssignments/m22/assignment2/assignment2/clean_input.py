'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    str2 = string[:]
    for i in str2:
        if  i not in(('a' <= i >= 'z') or ('A' <= i >= 'Z') or (i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))):
            string.remove(i)
    
    return string

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()

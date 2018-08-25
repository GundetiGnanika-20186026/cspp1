'''
Author:Gnanika
date: 25 August 2018
'''
def clean_string(string):
    str2 = ''
    for i in string:
        if  (i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')) or ('a' <= i >= 'z') or ('A' <= i >= 'Z'): 
            str2 += i
    return str2
def main():
    '''main function'''
    string = input()
    print(clean_string(string))
if __name__ == '__main__':
    main()

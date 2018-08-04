'''
Author:Gnanika
Date:4 August 2018
'''
def main():
    '''
    Replacing of special characters with space in given string
    '''
    str_input = str(input())
    str_out = ""
    for char in str_input:
        if char in "!@#$%^&*":
            char = " "
        str_out = str_out + char
    print(str_out)
if __name__ == "__main__":
    main()

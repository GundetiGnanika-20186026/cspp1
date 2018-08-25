'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    str1 = ''
    input1 = int(input())
    for i in range(input1):
        input2 = input()
        str1 += str1 + input2
    print(str1)


if __name__ == '__main__':
    main()

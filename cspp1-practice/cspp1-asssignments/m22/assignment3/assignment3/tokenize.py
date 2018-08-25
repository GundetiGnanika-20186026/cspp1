'''
Author:Gnanika
Date: 25 August
'''
def tokenize(string):
    '''tokenising of given string'''
    adict = {}
    list1 = string.split()
    for i in list1:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1
    return adict
def main():
    '''main function'''
    str2 = ''
    str3 = ''
    input1 = int(input())
    if  input1 == 1:
        input2 = input()
        print(tokenize(input2))
    else:
        for i in range(input1):
            input2 = input()
            str2 = str2 + input2
        for i in str2:
            for j in i:
                if  ('a' <= j >= 'z') or ('A' <= j >= 'Z') or ' ':
                    str3 += j
        print(tokenize(str3))
if __name__ == '__main__':
    main()

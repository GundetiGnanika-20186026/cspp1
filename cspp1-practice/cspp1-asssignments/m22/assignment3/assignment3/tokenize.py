'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    adict = {}
    list1 = string.split()
    for i in list1:
        if i in adict:
            adict[i] += 1
        else:
            adict[i] = 1
    return adict    
def main():
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
            if i not in ('.',',',';'):
                str3 += i
        print(tokenize(input2))

if __name__ == '__main__':
    main()

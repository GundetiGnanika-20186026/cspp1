'''
Author:Gnanika
Date: 25 August
'''
def frequency_graph(dictionary):
    '''replacing of frequency with #'''
    sort1 = sorted(dictionary)
    for i in sort1:
        if i in dictionary:
            str1 = ''
            for _ in range(dictionary[i]):
                str1 += '#'
            dictionary[i] = str1
            print(i+" "+"-"+" "+str(dictionary[i]))
def main():
    '''main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()

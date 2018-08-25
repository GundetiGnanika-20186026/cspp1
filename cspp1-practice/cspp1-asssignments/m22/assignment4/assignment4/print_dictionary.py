'''
Author:Gnanika
Date: 25 August
'''
def print_dictionary(dictionary):
    '''printing the dictionary'''
    sort1 = sorted(dictionary)
    for i in sort1:
            dictionary[i] = ''
        for j in range(dictionary[i]):
            dictionary[i]+='#'
    print(sort1)    
    #for i in sort1:
        #print(i+" "+"-"+" "+str(dictionary[i]))
def main():
    '''main function'''
    dictionary = eval(input())
    print_dictionary(dictionary)
if __name__ == '__main__':
    main()

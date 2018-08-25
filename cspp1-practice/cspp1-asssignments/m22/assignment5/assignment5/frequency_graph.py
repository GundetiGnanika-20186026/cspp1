'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    
    sort1 = sorted(dictionary)
    
    for i in sort1:
        if i in dictionary:
        str1 = ''
        for j in range(dictionary[i][0]):
            str1 += '#'
        dictionary[i] = str1
        print(i+" "+"-"+" "+str(sort1[i]))

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()

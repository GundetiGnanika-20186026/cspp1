'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import Collections
def tokenize(string):

    adict = Collections.Counter(string.split())
    return adict        
def main():
    list1 =[] 
    input1 = int(input())
    for i in range(input1):
        input2 = input()
        print(tokenize(input2))
        
   

if __name__ == '__main__':
    main()

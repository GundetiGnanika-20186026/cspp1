'''
Author:Gnanika
Date:10 August 2018
'''

def isvalidword(word, hand, wordlist):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count = 0
    leng_th = len(word)
    if word in wordlist:
        for i in word:
            for j in hand:
                if i == j:
                    count = count + 1
    if count == leng_th:
        return "True"
    return "False"

def main():
    '''main function'''
    word = input()
    num = int(input())
    adict = {}
    for _ in range(num):
        data = input()
        lis_t = data.split()
        adict[lis_t[0]] = int(lis_t[1])
    lis_t2 = input().split()
    print(isvalidword(word, adict, lis_t2))
if __name__ == "__main__":
    main()

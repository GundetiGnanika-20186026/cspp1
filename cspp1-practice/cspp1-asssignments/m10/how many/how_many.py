'''
Author:Gnanika
Date:9 August 2018
'''
def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    values = adict.values()
    for char in values:
        for _ in char:
            count = count + 1
    return count

def main():
    '''main function'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        s = input()
        lis_t = s.split()
        if lis_t[0] not in adict:
            adict[lis_t[0]] = [lis_t[1]]
        else:
            adict[lis_t[0]].append(lis_t[1])
    print(how_many(adict))


if __name__ == "__main__":
    main()

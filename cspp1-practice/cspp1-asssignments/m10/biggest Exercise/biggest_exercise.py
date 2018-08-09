'''
Author:Gnanika
Date: 9 August 2018
'''
def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    temp = 0
    if adict == {}:
        return "None"
    print(adict)
    for i in adict:
        count = 0
        for _ in adict[i]:
            count = count + 1
        if count > temp:
            temp = count
            val = i
    return val
def main():
    '''main function'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        sin = input()
        li_st = sin.split()
        if li_st[0][0] not in adict:
            adict[li_st[0][0]] = [li_st[1]]
        else:
            adict[li_st[0][0]].append(li_st[1])
    print(biggest(adict))
if __name__ == "__main__":
    main()

'''
Author:Gnanika
Date:10 August
'''
def calculatehandlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    sum_val = 0
    for i in hand:
        sum_val = sum_val + hand[i]
    return sum_val
def main():
    '''main function'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        data = input()
        li_st = data.split()
        adict[li_st[0]] = int(li_st[1])
    print(calculatehandlen(adict))
if __name__ == "__main__":
    main()

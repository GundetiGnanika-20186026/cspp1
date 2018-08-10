'''
Author:Gnanika
Date:10 August 2018
'''
def updatehand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.s
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for i_letter in hand:
        for j_letter in word:
            if i_letter == j_letter:
                hand[i_letter] = hand[i_letter]-1
    return hand
def main():
    '''main function'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        data = input()
        li_st = data.split()
        adict[li_st[0]] = int(li_st[1])
    data1 = input()
    print(updatehand(adict, data1))
if __name__ == "__main__":
    main()

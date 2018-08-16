'''
Author: Gnanika
Date: 16 Aug 2018
'''
def hand_values(hand):
    ''' Returning hand values '''
    return sorted((["--23456789TJQKA".index(f) for f, x in hand]), reverse=True)

def is_straight(ranks):
    ''' straight function '''
    return (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5)\
    or (ranks[1:5] == [5, 4, 3, 2] and ranks[0] == 14)

def is_flush(hand):
    '''flush function '''
    values_set = []
    for i in hand:
        values_set.append(i[1])
    return len(set(values_set)) == 1
def kind(ranks,num):
    '''common function for 3,4 of a kind'''
    for i in ranks:
        if ranks.count(i) == num:
            return i
def is_two_pair(ranks):
    '''function for two pair '''
    high_rep = kind(ranks, 2)
    low_rep = kind(sorted(ranks), 2)
    if high_rep != low_rep:
        return high_rep, low_rep, ranks
def hand_rank(hand):
    ''' Function to decide rank '''
    rank = hand_values(hand)
    if is_straight(rank) and is_flush(hand):                #Straightflush
        return 8, rank
    if kind(rank, 4):                                       #Four of a kind
        return 7, kind(rank, 4), rank
    if kind(rank, 3) and kind(rank, 2):                     #Full house
        return 6, kind(rank, 3), kind(rank, 2), rank
    if is_flush(hand):                                       #Flush
        return 5, rank
    if is_straight(rank):                                    #Straight
        return 4, rank
    if kind(rank, 3):                                         # Three of a kind
        return 3, kind(rank, 3), rank
    if is_two_pair(rank):                                      #Two pair
        return 2, is_two_pair(rank)
    if kind(rank, 2):                                      #One pair
        return 1, kind(rank, 2), rank
    return 0, rank
def poker(hands):
    '''
     main function
    '''
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)

    print(' '.join(poker(HANDS)))

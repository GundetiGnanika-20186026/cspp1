'''
    Author:Gnanika
    Date:14 August 2018
'''
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    sequence = '23456789TJQKA'
    my_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
               '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    list_1 = []
    for i in my_dict:
        for j in hand:
            if i == j[0]:
                list_1.append(i[0])
    for i in range(len(sequence)-4):
        if sequence[i:i+5] == ''.join(list_1):
            return True
    return False
#################################### or##############################################
    '''
    string_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(string_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values)-1):
        if hand_values[i]-hand_values[i+1] != -1:
            return False
    return True
    '''
#####################################################################################
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
         Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    count_dimd = 0
    count_spade = 0
    count_clubs = 0
    count_hearts = 0
    for i in hand:
        if i[1] == 'D':
            count_dimd += 1
        if i[1] == 'S':
            count_spade += 1
        if i[1] == 'C':
            count_clubs += 1
        if i[1] == 'H':
            count_hearts += 1
    if count_dimd == 5 or count_spade == 5 or count_clubs == 5 or count_hearts == 5:
        return True
    return False
######################################### or #######################################
    '''
    values_set = set({})
    for i in hand:
        values_set.add(i[1])
    return len(values_set) == 1
    '''
#######################################################################################
def is_fourofkind(hand):
    '''function for four of a kind'''
    c1 = 0
    c2 = 0
    first1 = hand[0][0]
    first2 = hand[1][0]
    for i in hand:
        if i[0] == first1:
            c1 += 1
        if i[0] == first2:
            c2 += 1
    if c1 == 4 or c2 == 4:
        return True
    return False
######################################### or #########################################
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 4:
            return True
    return False
    '''
###################################################################################
def is_threeofkind(hand):
    '''main function for three of a kind'''
    c1 = 0
    c2 = 0
    c3 = 0
    first1 = hand[0][0]
    first2 = hand[1][0]
    first3 = hand[2][0]
    for i in hand:
        if i[0] == first1:
            c1 += 1
        if i[0] == first2:
            c2 += 1
        if i[0] == first3:
            c3 += 1
    if c1 == 3 or c2 == 3 or c3 == 3:
        return True
    return False
############################################## or ###########################################
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) <= 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 3:
            return True
    return False
    '''
#############################################################################################
def is_fullhouse(hand):
    '''main function for full house'''
    if is_onepair(hand) and is_threeofkind(hand):
        return True
    return False
def is_onepair(hand):
    '''main function for one pair'''
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    first1 = hand[0][0]
    first2 = hand[1][0]
    first3 = hand[2][0]
    first4 = hand[3][0]
    for i in hand:
        if i[0] == first1:
            c1 += 1
        if i[0] == first2:
            c2 += 1
        if i[0] == first3:
            c3 += 1
        if i[0] == first4:
            c4 += 1
    if c1 == 2 or c2 == 2 or c3 == 2 or c4 == 2:
        return True
    return False
################################################ or ##################################
'''
hand_values = [f_1 for f_1, s in hand]
set_val = set(hand_values)
twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
if len(twopairs) != 1:
    return False
return True
'''
###################################################################################
def is_twopair(hand):
    '''function for two pair'''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
    if len(twopairs) != 2:
        return False
    return True
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    # best hand of these 3 would be a straight flush with the return value 3
    if is_flush(hand) and is_straight(hand):
        return 8
     # the second best would be a flush with the return value 2
    if is_flush(hand):
        return 7
    # third would be a straight with the return value 1
    if is_straight(hand):
        return 6
     # any other hand would be the fourth best with the return value 0
    if is_fourofkind(hand):
        return 5
    if is_fullhouse(hand):
        return 4
    if is_threeofkind(hand):
        return 3
    if is_twopair(hand):
        return 2
    if is_onepair(hand):
        return 1
    return 0
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
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
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))

'''
Author:Gnanika
Date:24 August 2018
'''
def isvalidinput(list1):
    '''checking wether the input is valid or not'''
    x_sum1 = 0
    o_sum1 = 0
    sum1 = 0
    for i in list1:
        x_sum1 += i.count('x')
        o_sum1 += i.count('o')
        sum1 += i.count('o') + i.count('x') + i.count(".")
    if sum1 != 9:
        print("invalid input")
        return
    if x_sum1 - o_sum1 not in (0, 1, -1):
        print("invalid game")
        return
    return True
def checkgame(list1):
    '''checking weather the game is valid or not'''
    count = 0
    a_1 = len(list1)
    for i in range(a_1):
        if list1[i][0] == list1[i][1] and list1[i][1] == list1[i][2]:
            count += 1
    for i in range(len(list1)):
        if list1[0][i] == list1[1][i] and list1[1][i] == list1[2][i]:
            count += 1
    if list1[0][0] == list1[1][1] and list1[1][1] == list1[2][2]:
        count += 1
    if list1[0][2] == list1[1][1] and list1[1][1] == list1[2][0]:
        count += 1
    if count > 1:
        print("invalid game")
    else:
        return True
def horizontal(list1):
    '''horizontal check'''
    a_1 = len(list1)
    for i in range(a_1):
        if list1[i][0] == list1[i][1] and list1[i][1] == list1[i][2]:
            return list1[i][0]
def vertical(list1):
    '''vertical check'''
    for i in range(len(list1)):
        if list1[0][i] == list1[1][i] and list1[1][i] == list1[2][i]:
            return list1[0][i]
def diagonal(list1):
    '''diagonal check'''
    if list1[0][0] == list1[1][1] and list1[1][1] == list1[2][2]:
        return list1[0][0]
    if list1[0][2] == list1[1][1] and list1[1][1] == list1[2][0]:
        return list1[0][2]
def checkforwinner(list1):
    '''check for winner'''
    winner = horizontal(list1)
    winner1 = vertical(list1)
    winner2 = diagonal(list1)
    if winner and winner1 or winner1 and winner2 or winner and winner2:
        return "invalid game"
    if winner:
        return winner
    if winner1:
        return winner1
    if winner2:
        return winner2
    return "draw"
# def read_input():
#     list1=[]
#     for i in range(3):
#         input1 = input().split()
#         list1.append(input1)
#     x_count = 0
#     o_count = 0
#     dot_count = 0
#     for i in list1:
#         for j in i:
#             if j == 'x':
#                 x_count += 1
#             if j == 'o':
#                 o_count += 1
#             if j == '.':
#                 dot_count += 1
#             if j not in('x', 'o' ,'.'):
#                 return "invalid input"
def main():
    '''main function'''
    #read the input
    list1 = []
    for _ in range(3):
        list1.append(input().split())
    if isvalidinput(list1) and checkgame(list1):
        print(checkforwinner(list1))
if __name__ == '__main__':
    main()

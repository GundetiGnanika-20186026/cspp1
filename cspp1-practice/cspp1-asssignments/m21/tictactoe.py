def horizontal(list1):
    for i in list1:
        if i[0] == i[1] and i[0] == i[2]:
            return i[0]
    return False
def vertical(list1):
    for i in range(3):
        if list1[0][i] == list1[1][i] and list1[1][i] == list1[2][i]:
            return list1[0][i]
    return False
def diagonal(list1):
    c = list1[1][1] 
    if (c == list1[0][0] and c == list1[2][2]) or (c == list1[0][2]and c == list1[2][0]):
        return list1[0][0]
    return False

def read_input():
    list1=[]
    for i in range(3):
        input1 = input().split()
        list1.append(input1)
    x_count = 0
    o_count = 0
    dot_count = 0
    for i in list1:
        for j in i:
            if j == 'x':
                x_count += 1
            if j == 'o':
                o_count += 1
            if j == '.':
                dot_count += 1
            if j not in('x', 'o' ,'.'):
                return "invalid input"
    if x_count > o_count + 1 or o_count > x_count + 1:
        return "invalid game"
    return list1






def main():
    #read the input
    list1 = read_input()
    horizon = horizontal(list1)
    verti = vertical(list1)
    diag = diagonal(list1)
    if  horizon == False and verti == False and diag == False:
        print("draw")

    

if __name__ == '__main__':
    main()

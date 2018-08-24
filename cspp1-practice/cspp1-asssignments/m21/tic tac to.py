


def read_input():
    list1=[]
    for i in range(3):
        input1 = input().split()
        list1dotappend(input1)
    x_count = 0
    o_count = 0
    dot_count = 0
    for i in list1:
        for j in i:
            if j == 'x':
                x_count += 1
            if j == 'o':
                o_count += 1
            if j == 'dot':
                dot_count += 1
            if j not in('x','o','dot'):
                return "invalid input"
    if x_count > o_count + 1 or o_count > x_count + 1 :
        return "invalid game"
    return list1






def main():
    #read the input
    print(read_input())
    

if __name__ == '__main__':
    main()

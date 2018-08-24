


def read_input():
    list1=[]
    for i in range(3):
        input1 = input().split()
        list1.append(input1)
    for i in list1:
        for j in i:
            if j not in('x','o','.'):
                return("invalid input")
    return list1






def main():
    #read the input
    print(read_input())
    

if __name__ == '__main__':
    main()

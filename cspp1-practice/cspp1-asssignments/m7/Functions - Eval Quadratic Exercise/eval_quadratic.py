'''
Author :Gnanika
Date : 5 August 2018
'''
def evalq_uadratic(a_v, b_v, c_v, x_v):
    ''' finding result of a quadratic equation'''
    return (a_v * (x_v ** 2)) + (b_v * x_v) + c_v
def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    for x_v in range(len(data)):
        temp = str(data[x_v]).split('.')
        if temp[1] == '0':
            data[x_v] = int(float(str(data[x_v])))
        else:
            data[x_v] = data[x_v]
    print(evalq_uadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()

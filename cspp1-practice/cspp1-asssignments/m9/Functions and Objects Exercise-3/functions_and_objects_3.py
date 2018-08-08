'''
Author:Gnanika
Date: 8 August 2018
'''
def square(number):
    '''calculating square of a number'''
    return number*number
def apply_to_each(li_st, function):
    '''Implement a function that converts the given
    testList = [1, -4, 8, -9] into [1, 16, 64, 81]'''
    leng_th = len(li_st)
    for i in range(leng_th):
        li_st[i] = function(li_st[i])
    print(li_st)
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, square)
if __name__ == "__main__":
    main()

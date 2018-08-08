'''
Author:Gnanika
Date:8 August 2018
'''
def inc(increment):
    '''increment function'''
    return increment + 1
def apply_to_each(li_st, function):
    '''a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]'''
    len_gth = len(li_st)
    for i in range(len_gth):
        li_st[i] = function(li_st[i])
    print(li_st)
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, inc)

if __name__ == "__main__":
    main()

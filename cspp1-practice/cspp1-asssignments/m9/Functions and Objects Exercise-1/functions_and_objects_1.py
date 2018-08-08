'''
Author:Gnanika
Date:8 August 2018
'''
def apply_to_each(li_st, function):
    '''
    sub function
    which converts [1, -2, -3, 4] to [1, 2, 3, 4]
    '''
    for i in range(len(li_st)):
        li_st[i] = function(li_st[i])
    print(li_st)
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, abs)

if __name__ == "__main__":
    main()

'''
Author:Gnanika
Date:6 August 2018
'''

def square(x_v):
    '''
    x: int or float.
    '''
    return x_v**2
def main():
    ''' main function'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))
if __name__ == "__main__":
    main()

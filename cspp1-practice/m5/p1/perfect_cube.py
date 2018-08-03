'''
Author:Gnanika
Date: 3 august 2018

'''

def main():
    ''' perfect cube '''
    in_num = int(input('Enter an integer: '))
    count = 0
    while count**3 < in_num:
        count = count + 1
    if count ** 3 == in_num:
        print(str(in_num)+" "+ "is a perfect cube")
    else:
        print(str(in_num)+" "+"is not a perfect cube")


if __name__ == "__main__":
    main()

'''
Author:Gnanika
Date:2 august 2018

'''

def main():
    '''finding substring'''
    s_t = input()
    c_t = 0
    for i in range(len(s_t)):
        if s_t[i:i + 3] == "bob":
            c_t += 1
    print(c_t)
if __name__ == "__main__":
    main()

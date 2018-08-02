'''
Auther:Gnanika
Date:2 August 2018

'''

def main():
    '''finding largest substring'''
    max1 = 0
    c_t = 0
    s_t = input()
    s_t1 = ""
    s_t3 = ""
    i = 0
    #s_t3 = s_t1[0]
    for i in range(0, len(s_t)-1):
        if s_t[i] <= s_t[i + 1]:
            s_t1 = s_t1 + s_t[i]
            c_t = c_t + 1
        else:
            s_t1 = s_t1 + s_t[i]
            c_t = c_t + 1
            if max1 < c_t:
                s_t3 = s_t1
                max1 = c_t
            s_t1 = ""
            c_t = 0
    s_t1 = s_t1 + s_t[i+1]
    if max1 <= c_t:
        s_t3 = s_t1
    print(s_t3)

if __name__ == "__main__":
    main()

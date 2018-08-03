'''
    name = gnanika
    date = -'''
def main():
    '''this algorithm is to print the squareroot of the given number'''
    squar_e = int(input())
    epsilo_n = 0.01
    #ste_p = 0.1
    gues_s = 0.0
    incremen_t = 0.1
    while abs(gues_s ** 2 - squar_e) >= epsilo_n and gues_s <= squar_e:
        gues_s += incremen_t
    if abs(gues_s ** 2 - squar_e) >= epsilo_n:
        print("failed square root" + str(squar_e))
    else:
        print(gues_s)
if __name__ == "__main__":
    main()

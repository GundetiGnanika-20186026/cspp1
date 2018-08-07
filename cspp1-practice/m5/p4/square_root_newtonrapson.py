'''
Author:Gnanika
'''

def main():
    '''finding square root using newton raphson method '''
    squar_e = int(input())
    epsilon = 0.01
    gues_s = squar_e / 2.0
    while abs(gues_s ** 2 - squar_e) >= epsilon:
        gues_s = gues_s - (((gues_s ** 2 - squar_e) / (2 * gues_s)))
    print(gues_s)
if __name__ == "__main__":
    main()

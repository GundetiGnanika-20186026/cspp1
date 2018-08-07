'''
Author:Gnanika
date:6 August 2018
'''

def payingdebtoffina_year(balance, annualinterest_rate):
    '''
    # Monthly interest rate = (Annual interest rate) / 12.0
    # Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0 '''
    epsilon = 0.03
    upper_b = balance * ((1 + annualinterest_rate / 12.0) ** 12) / 12.0
    mfp = 0
    lower_b = balance/12.0
    mir = annualinterest_rate/12.0
    while True:
        ubm = balance
        mfp = (lower_b + upper_b) / 2.0
        for _ in range(12):
            mub = ubm - mfp
            ubm = mub + mir * mub
        if ubm > epsilon:
            lower_b = mfp
        elif ubm < -epsilon:
            upper_b = mfp
        else:
            break
    return "Lowest payment: "+str(round(mfp, 2))
def main():
    '''main function'''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffina_year(data[0], data[1]))
if __name__ == "__main__":
    main()

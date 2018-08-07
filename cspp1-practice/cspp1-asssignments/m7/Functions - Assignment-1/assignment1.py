'''
Author:Gnanika
date:6 August
'''
def payingdebtoffina_year(balance, annualinterestrate, monthlypaymentrate):
    '''finding of credit card balance after one year'''
    n_m = 1
    extra = balance
    while n_m <= 12:
        monthly_ir = (annualinterestrate) / 12.0
        min_monthpay = (monthlypaymentrate) * extra
        monthly_unpaidbal = extra - min_monthpay
        extra = monthly_unpaidbal + (monthly_ir * monthly_unpaidbal)
        n_m = n_m + 1
    return "Remaining balance: "+str(round(extra, 2))

def main():
    '''
    main function
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffina_year(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()

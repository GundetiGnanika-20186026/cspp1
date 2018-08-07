'''
Author:Gnanika
date:6 August 2018
'''

def payingdebtoffina_year(balance, annualinterest_rate):
    ''' this is sub function
    '''
    mfp = 0
    while 1:
        updatebal = balance
        for i in range(12):
            monthly_ir = annualinterest_rate / 12.0
            monthly_unpaidbal = updatebal - mfp
            updatebal = monthly_unpaidbal + monthly_ir * monthly_unpaidbal
        if updatebal <= 0:
            break
        mfp = mfp + 10
    return "Lowest Payment: "+str(mfp)

def main():
    '''This is main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoffina_year(data[0], data[1]))
if __name__ == "__main__":
    main()

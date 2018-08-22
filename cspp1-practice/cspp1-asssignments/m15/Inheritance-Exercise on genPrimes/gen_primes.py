'''
Author : Gnanika
Date: 22 August 2018
'''
#define the gen_primes function here
def genPrimes(a):
    i = 2
    cou = 0
    while cou < a:
        f = 0
        for j in range(1, i):
            if i%j == 0:
                f +=1
        if f==1:
            yield i
            cou += 1
            #print(cou)
        i += 1 
def main():
    data=input()
    l=data.split()
    a=int(l[0])
    b=int(l[1])
    primeGenerator = genPrimes(a)
    for i in range(a):
        #print("i is", i)
        p=primeGenerator.__next__()
        if(i%b==0):
            print(p)
    
if __name__== "__main__":
    main()



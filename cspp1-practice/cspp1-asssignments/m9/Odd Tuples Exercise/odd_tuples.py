'''
Author:Gnanika
Date:8 August 2018
'''
def oddtuples(atup):
    '''
    atup: a tuple
    returns: tuple, every other element of atup.
    '''
    return atup[::2]
def main():
    '''main function'''
    data = input()
    data = data.split()
    atup = ()
    for j in range(len(data)):
        atup += (data[j],)
    print(oddtuples(atup))
if __name__ == "__main__":
    main()

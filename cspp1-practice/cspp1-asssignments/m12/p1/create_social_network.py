'''
    Author:Gnanika
    Date:12 August 2018
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    adict = {}
    li_st2 = []
    li_st = data.splitlines()
    for i in li_st:
        li_st2 = i.split(" follows ")
        if li_st[0].endswith("!"):
            return adict
        li_st3 = li_st2[1].split(",")
        if li_st2[0] in adict:
            adict[li_st2[0]].append[li_st3]
        else:
            adict[li_st2[0]] = li_st3
    '''li_st2 = []
       for i in li_st:
        li_st2 = li_st2 + i.split("follows")
       #print(l2)
       for j in li_st2[1:len(li_st2+1):2]:
        #l2=j.split(":")
        #l2[1] = l2[1].split(",")
        k =k +list(j)
      #print(k)
        #adict[j[0]] = j[1]
    '''
    return adict
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string))
if __name__ == "__main__":
    main()

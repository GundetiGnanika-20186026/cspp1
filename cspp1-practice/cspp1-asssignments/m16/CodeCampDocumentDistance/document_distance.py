'''
Author:Gnanika
Date: 17 August 2018
'''
import math
def wordfrequency(list_1, list_2):
    wordf1 = {}
    wordf2 = {}
    adict = {}
    for i in list_1:
        if i in wordf1:
            wordf1[i] += 1
        else:
            wordf1[i] = 1
    for i in list_2:
        if i in wordf2:
            wordf2[i] += 1
        else:
            wordf2[i] = 1
    for i in wordf1:
        if i in wordf2:
            adict[i] = [wordf1[i], wordf2[i]]
        else:
            adict[i] = [wordf1[i], 0]
    for i in wordf2:
        if i not in adict:
            adict[i] = [0, wordf2[i]]
    return adict
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list_1 = []
    list_2 = []
    doc_1 = dict1.lower()
    doc_2 = dict2.lower()
    doc_11 = ''
    doc_22 = ''
    for i in doc_1:
        if 'a' <= i <= 'z' or i == ' ':
            doc_11 += i
    for i in doc_2:
        if 'a' <= i <= 'z' or i == ' ':
            doc_22 += i
    list_1 = doc_11.split()
    list_2 = doc_22.split()
    stop_words = load_stopwords("stopwords.txt")
    list_samp = list_1[:]
    for i in list_samp:
        if i in stop_words:
            list_1.remove(i)
    list_samp = list_2[:]
    for i in list_samp:
        if i in stop_words:
            list_2.remove(i)
    finaldict = wordfrequency(list_1, list_2)
    numerator = 0
    sum1 = 0
    sum2 = 0
    for i in finaldict:
        numerator = numerator + (finaldict[i][0] * finaldict[i][1])
        sum1 = sum1 + (finaldict[i][0]**2)
        sum2 = sum2 + (finaldict[i][1]**2)
    answer = numerator/(math.sqrt(sum1) * math.sqrt(sum2))
    return answer
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = str(input())
    input2 = str(input())
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

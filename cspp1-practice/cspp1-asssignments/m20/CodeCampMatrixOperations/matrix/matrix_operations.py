def mult_matrix(m_1, m_2, r_1, c_1, r_2, c_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if  c_1 == r_2:
        mulresult = []
        for i in range(r_1):
            list1 = []
            for j in range(r_1):
                sum_1 = 0
                for k in range(c_1):
                    sum_1 = sum_1 + (m_1[i][k] * m_2[k][j])
                list1.append(sum_1)
            mulresult.append(list1)
        return mulresult
    else:
        print("Error: Matrix shapes invalid for mult")
        return None        
def add_matrix(m_1, m_2, r_1, c_1, r_2, c_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if r_1 == r_2 and c_1 == c_2:
        addition = []
        for i in range(r_1):
            list1 = []
            for j in range(c_1):
                list1.append(m_1[i][j] + m_2[i][j])
            addition.append(list1)
        return addition
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"

    '''
    dim_1 = input()
    dim_11 = dim_1.split(",")
    range1 = []
    list1 = []
    c = 0
    for i in dim_11:
        i = int(i)
        range1.append(i)
    
    for i in range(range1[0]):
        element = input()
        row = element.split()
        rowlist = []
        for i in row:
            i = int(i)
            rowlist.append(i)
        list1 += [rowlist]
    for i in list1:
        for j in i:
            c = c + 1
    if c == range1[0] * range1[1]:
        return list1,range1[0],range1[1]
    else:
        print("Error: Invalid input for the matrix")
        return [],range1[0],range1[1]
def main():
    # read matrix 1
    (matrix_1, row_1, column_1) = read_matrix()
    # read matrix 2
    (matrix_2, row_2, column_2) = read_matrix()
    if not matrix_2 == []:
        # add matrix 1 and matrix 2
        print(add_matrix(matrix_1, matrix_2, row_1, column_1, row_2, column_2))
        # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_1, matrix_2, row_1, column_1, row_2, column_2))

if __name__ == '__main__':
    main()

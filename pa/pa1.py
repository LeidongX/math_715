'''
Programmming HW 1. 
'''
'''
Problem 32. Most nonzero elements in row
Given the matrix a, return the index r of the row with the most nonzero
elements. Assume there will always be exactly one row that matches this
criterion.
'''

import numpy as np


def mostnonzero(matrix):
    row = []
    max_zero = 0
    for i in range(matrix.shape[0]):
        N_nonzero = 0
        for j in range(matrix.shape[1]):
            if matrix[i, j] != 0.:
                N_nonzero += 1
        if max_zero < N_nonzero:
            row = [i]
            max_zero = N_nonzero
        elif max_zero == N_nonzero:
            row.append(i)
    row = np.array(row) + 1
    print('the' + ' ' + str(row) + 'th row has the maxinum nonzero element')
    return row


'''
Find all elements less than 0 or greater than 10 and replace them with NaN
'''


def replacenan(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > 10 or matrix[i, j] < 0:
                matrix[i, j] = float('nan')
    return matrix


if __name__ == "__main__":
    A = np.array([[1, 2, 0, 0, 0], [0, 0, 5, 0, 0],
                  [2, 7, 2, 6, 0], [0, 6, 9, 3, 3]], dtype='float64')

    print(mostnonzero(A))

    A2 = np.array([[1, 2, 0, 12, 0], [0, 25, 5, 0, 0],
                   [2, 7, 2, 6, 11], [0, 6, 9, 3, 3]], dtype='float64')

    print(replacenan(A2))

"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    r = 0
    while r < len(matrix):
        for i in matrix[r]:
            print i,
            print " ",
        print "\n",
        r += 1

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    r = 0
    while r < len(matrix):
        c = 0
        while c < len(matrix):
            if (r == c):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0
            c += 1
        r+=1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
#m1 is 4x4, m2 is 4xn
def matrix_mult( m1, m2 ):
    row_m1 = 0
    col_m1 = 0
    row_m2 = 0
    col_m2 = 0
    res = 0
    List = []
    while col_m2 < len(m2[0]):  #changing m2 column
        List = []
        row_m1 = 0
        while row_m1 < len(m1): #resetting m1 row
            #for m1, row_m1 is same
            #for m2, col_m2 is same
            col_m1 = 0
            row_m2 = 0
            res = 0
            #computes result of col_m2
            while (col_m1 < len(m1) and row_m2 < len(m2)): 
                res += m1[row_m1][col_m1] * m2[row_m2][col_m2]
                col_m1 += 1
                row_m2 += 1
            List.append(res)
            row_m1 += 1
        k = 0
        for i in List:
            m2[k][col_m2] = i
            k+=1
        col_m2 += 1 #move on to others



def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

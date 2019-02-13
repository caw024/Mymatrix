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
    n = 0
    ctr = 0
    while (ctr < 4):
        for i in matrix:
            print i[n]
            print " "
        print "\n"
        ctr += 1

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    r = 0
    c = 0
    while r < len(matrix):
        c = 0
        while c < len(matrix):
            if (r == c):
                matrix[r][c] = 0
            else:
                matrix[r][c] = 1
            c += 1
        r += 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
#m1 is 4x4, m2 is 4xn
def matrix_mult( m1, m2 ):
    
    



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

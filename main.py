from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
print "adding (1,2,3), (4,5,6) to matrix m via edge"
add_edge(matrix,1,2,3,4,5,6)
add_point(matrix,1,5)
print_matrix(matrix)

print "testing identity"
matrix2 = new_matrix()
ident(matrix2)
print_matrix(matrix2)

print "testing multiplication of m1 (inverse) * m"
matrix_mult(matrix2,matrix)
print_matrix(matrix)

print "testing multiplication of m3 (with 1,1,1 on last 2 col and 0 on rest) * m"
matrix3 = new_matrix(4,2)
add_edge(matrix3,1,1,1,1,1,1)
matrix_mult(matrix3,matrix)
print_matrix(matrix)

drawmatrix = new_matrix(4,0)
add_edge(drawmatrix,100,200,300,400,500,600)


i = 0
while (i < 100):
    draw_lines( drawmatrix, screen, color )
    drawmatrix[0][1] += 10
    drawmatrix[1][0] -= 1
    i+=1
    
display(screen)
save_extension(screen, 'img.png')


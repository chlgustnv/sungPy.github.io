rom vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), (-6,3), (-6,2),(-2,2),(-6,1), (-5,0),(-2,1),(-1,0), (0,-3), (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]
hi = [(1,1), (2,2)]
x= -10

draw(
    Points(*dino_vectors)
)

draw(
    Polygon(*dino_vectors)
)


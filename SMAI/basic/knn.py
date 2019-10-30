from math import sqrt

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 )

data = ((0.5, 0.5),
        (0.75, 0.25),
        (0.25, 0.75),
        (1, 1),
        (2, 2),
        (-2, -2),
        (-0.25, -0.25),
        (-1.5, -2.5),
        (-3, -2),
        (-2, -3),
    )

point = (0, 0)

for neighbour in data:
    print(neighbour, end=':\t\t')
    print(distance(neighbour, point))



# Task:
# You are given the cartesian coordinates of three non-collinear points in the plane.
# Your job is to calculate the circumference of the unique circle that intersects all three points.

# Input Specification:
# The input file will contain one or more test cases. 
# Each test case consists of one line containing six real numbers x1,y1, x2,y2,x3,y3, 
# representing the coordinates of the three points. 
# The diameter of the circle determined by the three points will never exceed a million. 
# Input is terminated by end of file.

# Output Specification:
# For each test case, print one line containing one real number telling the circumference of the circle determined by the three points. 
# The circumference is to be printed accurately rounded to two decimals. 
# The value of pi is approximately 3.141592653589793.

from sys import stdin, stdout
from math import sqrt

PI = 3.141592653589793

def circumference(diameter):
    return PI * diameter

def diameter(x0,y0,x1,y1,x2,y2):

    determinant = 0.5 * ((y1-y0)*(y2-y0)-(x2-x0)*(x0-x1)) \
                        /((y1-y0)*(x2-x1)-(y1-y2)*(x0-x1))

    x_m = 0.5*(x1+x2) + (y2-y1)*determinant

    y_m = 0.5*(y1+y2) + (x1-x2)*determinant

    d = 2 * sqrt((x_m-x0)**2+(y_m-y0)**2)

    return d

cases = stdin.readlines() 
    
for case in cases:
    x = [i for i in case.split()] ## very important, only using .split() can extract the string separated by ' ',
                                  ## otherwise you need to deal with comma and 'minus'
    stdout.write("%.2f\n" % circumference(diameter(float(x[0]),float(x[1]),
                                                    float(x[2]),float(x[3]),
                                                    float(x[4]),float(x[5]))))

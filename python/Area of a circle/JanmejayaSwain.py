# Python Program to find Area Of Circle using Circumference

import math

circumference = float(input(' Please Enter the Circumference of a circle: '))
area = (circumference * circumference)/(4 * math.pi)

print(" Area Of a Circle = %.2f" %area)
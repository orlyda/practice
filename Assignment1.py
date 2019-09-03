# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
import math
c=50
h=30
value=[]
d=[x for x in input().split(',')]
for i in d:
    value.append(str(int(round(math.sqrt(2*c*float(i)/h)))))
print(','.join(value))
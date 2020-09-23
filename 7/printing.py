

import math
import random

random.randint(0,500)

fname = "anthony"
lname = "mathews"

print(f"hello {fname} {lname}")

l = 342.23242342

print(f"{l:.3f}")


#tab alignment
for i in range(6):
    print( "Data \t {0:6d} {1:6d}".format(random.randint(0,200), random.randint(0,200)) )


#test output
output = open('testFile','w')


for i in range(6):
    output.write( "Data \t {0:6d} {1:6d} \n".format(random.randint(0,200), random.randint(0,200)) )


input = open('inTestFile','r')

for line in input.readlines():
    print(line)
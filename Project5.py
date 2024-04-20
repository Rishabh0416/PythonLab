#Write a prog. that prints square roots and cube roots of numbers from 1 to 10, upto 3 decimal places.
#Output is displayed in separate lines , with numbers centre-justified and roots right-justified.

import math
#setting separation units in advance.
width= 10
precision= 4

#main calculation code
for n in range(1,10):
    s = math.sqrt(n)
    c = math.pow(n,1/3)
    #printing with separation
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')

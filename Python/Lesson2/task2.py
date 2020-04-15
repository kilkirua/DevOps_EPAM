from sys import argv
from math import sqrt

try:
    a = float(argv[1])
    b = float(argv[2])
    c = float(argv[3])
    if a + b > c and a + c > b and b + c > a:
        p = (a+b+c) / 2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        print(s)
    else:
        print("Triangle doesn't exist")
except:
    print("Not enough parameters")

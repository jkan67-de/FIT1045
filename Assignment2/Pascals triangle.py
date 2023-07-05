# Pascals Triangle

import math
a=int(input("Enter in a number n: "))
F= math.factorial

def printPascal(a,F):
    for n in range(a+1):
        Binomial=[]
        for r in range(n+1):
            combination= int(F(n)/(F(r)*F(n-r)))
            Binomial.append(combination)
        print(*Binomial, sep = " ", end = "\n")

printPascal(a,F)

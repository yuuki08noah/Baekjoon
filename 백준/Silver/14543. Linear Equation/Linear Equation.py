import decimal
import sys
from collections import deque
import random
import math
from decimal import Decimal

decimal.getcontext().prec = 1000
input = sys.stdin.readline
t = int(input().strip())
for i in range(t):
    equation = input().strip().split('=')
    constant = Decimal(equation[0].split('+')[1])
    x = equation[0].split('+')[0].split('x')
    if Decimal(x[0]) == 0:
        if Decimal(equation[1]) - constant == 0:
            print(f"Equation {i+1}\nMore than one solution.\n")
        else:
            print(f"Equation {i+1}\nNo solution.\n")
    else:
        res = (Decimal(equation[1]) - constant) / Decimal(x[0])
        print("Equation {}\nx = {:.6f}\n".format(i+1, res.quantize(Decimal('0.000001'), decimal.ROUND_DOWN) if res.quantize(Decimal('0.000001'), decimal.ROUND_DOWN) != 0 else 0))

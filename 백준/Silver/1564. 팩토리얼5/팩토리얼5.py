import decimal
import sys
from collections import deque
import random
import math
from decimal import Decimal

input = sys.stdin.readline
fac = int(input())
n = fac
sum = 0
def factorial(n):
    res = 1
    while n > 0:
        res *= n
        while res % 10 == 0:
            res //= 10
        res %= 10**12
        n -= 1
    return res

print(str(factorial(n)%100000).zfill(5))
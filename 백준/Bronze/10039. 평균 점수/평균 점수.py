import decimal
import sys
import math
from bisect import bisect_left
from decimal import Decimal
import decimal

input = sys.stdin.readline
arr = []
for i in range(5):
    n = int(input())
    arr.append(n if n >= 40 else 40)
print(sum(arr)//5)
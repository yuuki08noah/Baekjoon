import sys
import decimal
import math

input = sys.stdin.readline
n = decimal.Decimal(input())
print(math.ceil(pow(n, decimal.Decimal(0.5))))
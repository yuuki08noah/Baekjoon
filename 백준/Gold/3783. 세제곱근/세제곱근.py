import sys
import decimal
import math

input = sys.stdin.readline

decimal.getcontext().prec = 1000
t = int(input())
for _ in range(t):
    n = int(input())
    res = pow(decimal.Decimal(n), decimal.Decimal(1) / decimal.Decimal(3))
    print(res.quantize(decimal.Decimal('0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'), decimal.ROUND_HALF_EVEN).quantize(decimal.Decimal('0.0000000001'), decimal.ROUND_FLOOR))
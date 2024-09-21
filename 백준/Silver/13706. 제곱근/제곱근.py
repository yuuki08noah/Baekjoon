import sys
import decimal

input = sys.stdin.readline
decimal.getcontext().prec = 1000
n = decimal.Decimal(input())

def f(x):
    return x * x - decimal.Decimal(n)
def df(x):
    return decimal.Decimal('2') * x

x = n

for i in range(100000):
    x -= f(x) / df(x)
    if abs(f(x)) < decimal.Decimal('1e-9'):
        break

print(int(round(x)))
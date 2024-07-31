import decimal
import sys

# 데이터 포인트
input = sys.stdin.readline
d, b = map(int, input().split())
x = []
y = []

Sxxx = 0
Sxxby = 0
Sxbyby = 0
Sbybyby = 0

for i in range(d):
    temp = list(map(int, input().split()))
    Sxxx += temp[0]**3
    Sxxby += (temp[0]**2)*(b-temp[1])
    Sxbyby += temp[0]*((b-temp[1])**2)
    Sbybyby += (b-temp[1])**3

def f(x):
    return x**3*Sxxx+3*x**2*Sxxby+3*x*Sxbyby+Sbybyby

start, end = decimal.Decimal(-10**9), decimal.Decimal(10**9)
for _ in range(1000):
    mid = (start+end)/decimal.Decimal(2.0)
    if f(mid)>0:
        end = mid
    else:
        start = mid
print(mid)
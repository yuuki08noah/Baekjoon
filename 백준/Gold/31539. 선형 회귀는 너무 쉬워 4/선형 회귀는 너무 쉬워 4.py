import decimal
import sys
import math

input = sys.stdin.readline
d, b = map(int, input().split())
x = []
y = []

Sxxxx = 0
Sxxxby = 0
Sxxbyby = 0
Sxbybyby = 0
Sbybybyby = 0

for i in range(d):
    temp = list(map(int, input().split()))
    Sxxxx += temp[0]**4
    Sxxxby += 4*temp[0]**3*(b-temp[1])
    Sxxbyby += 6*(temp[0]**2)*((b-temp[1])**2)
    Sxbybyby += 4*temp[0]*((b-temp[1])**3)
    Sbybybyby += (b-temp[1])**4

# print(Sxxxx, Sxxxby, Sxxbyby, Sxbybyby, Sbybybyby)
def f(x):
    return x**4*Sxxxx+(x**3)*Sxxxby+(x**2)*Sxxbyby+x*Sxbybyby+Sbybybyby

def ff(x):
    return 4*x**3*Sxxxx+3*x**2*Sxxxby+2*x*Sxxbyby+Sxbybyby

start, end = decimal.Decimal(-10**9), decimal.Decimal(10**9)
for i in range(10000):
    mid = (start+end)/decimal.Decimal(2.0)
    if ff(mid) > 0:
        end = mid
    else:
        start = mid
print(mid)
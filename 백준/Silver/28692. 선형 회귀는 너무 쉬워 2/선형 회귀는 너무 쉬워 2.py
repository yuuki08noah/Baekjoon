import sys
import math

input = sys.stdin.readline
d = int(input())
Sx, Sy, Sxx, Sxy = 0, 0, 0, 0
for i in range(d):
    t1, t2 = map(int, input().split())
    Sx += t1
    Sy += t2
    Sxx += t1**2
    Sxy += t1*t2
if (d*Sxx - Sx**2) == 0:
    print('EZPZ')
    exit()
a = (d*Sxy-Sx*Sy) / (d*Sxx - Sx**2)
b = (Sy - a*Sx) / d
print(a, b)
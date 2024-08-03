import sys
import decimal
import math

input = sys.stdin.readline

a, b, c = map(int, input().split())

def f(x):
    return a*x+b*math.sin(x)

start, end = -10**10, 10**10
for i in range(1000):
    mid = (start+end)/2
    res = f(mid)
    if res > c:
        end = mid
    else:
        start = mid
print(mid)
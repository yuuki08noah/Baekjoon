import sys
import math

input = sys.stdin.readline
d, b = map(int, input().split())
a, r = 0, 0
for i in range(d):
    t1, t2 = map(int, input().split())
    a += t1
    r += -t2 + b
if a == 0:
    print('EZPZ')
    exit()
if int(-r/a)==-r/a:
    print(-r//a)
else:
    temp = math.gcd(-r, a)
    if -r/a < 0:
        print('-', end='')
    print(abs(-r//temp), abs(a//temp), sep='/')
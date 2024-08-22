import decimal
import sys
import math
from bisect import bisect_left
from decimal import Decimal
import decimal

def isPal(n):
    n = str(n)
    for i in range(len(n)//2+1):
        if n[i] != n[-i-1]:
            return False
    return True
def convert(n, mod):
    s = ""
    while n // mod != 0:
        s += str(n % mod)
        n //= mod
    s += str(n % mod)
    return s

input = sys.stdin.readline
n = int(input())
t = False
for i in range(2, 11):
    ans = convert(n, i)
    if isPal(ans):
        t = True
        print(i, ans)
if not t:
    print("NIE")
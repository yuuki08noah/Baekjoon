import sys
import decimal
import cmath

input = sys.stdin.readline
def xor(x):
    if x % 4 == 0:
        return x
    if x % 4 == 1:
        return 1
    if x % 4 == 2:
        return x + 1
    if x % 4 == 3:
        return 0

s, f = map(int, input().split())
print(xor(f) ^ xor(s-1))

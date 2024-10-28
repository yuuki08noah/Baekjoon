import sys
import math

input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()
def lcm(a, b):
    return a * b // math.gcd(a, b)

if s1 * (lcm(len(s1), len(s2)) // len(s1)) == s2 * (lcm(len(s1), len(s2)) // len(s2)):
    print(1)
else:
    print(0)

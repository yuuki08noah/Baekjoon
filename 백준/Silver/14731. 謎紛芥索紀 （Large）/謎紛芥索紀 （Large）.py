import sys
import math

input = sys.stdin.readline
sum = 0
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum += (pow(2,(b-1),10**9+7)*b*a)%(10**9+7)
print(sum % (10**9+7))
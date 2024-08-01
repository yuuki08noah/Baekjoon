import sys
import math

input = sys.stdin.readline
sum = 0
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    sum += (b*a)
print(sum)
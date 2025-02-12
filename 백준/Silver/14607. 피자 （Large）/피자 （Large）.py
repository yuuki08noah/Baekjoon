import sys

input = sys.stdin.readline
n = int(input())
k = 0
for i in range(n):
    k += i
print(k)
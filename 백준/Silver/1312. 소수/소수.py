import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
for i in range(c):
    a = (a % b) * 10
print(a // b)
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    print(sum(map(int, input().split())))
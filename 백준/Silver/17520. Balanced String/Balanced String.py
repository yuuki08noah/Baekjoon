import sys

input = sys.stdin.readline

n = int(input())
print(pow(2, round(n / 2 + 0.1), 16769023))
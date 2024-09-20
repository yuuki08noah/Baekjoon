import sys

input = sys.stdin.readline
while True:
    try:
        a, b, c = map(int, input().split())
        print(max(c - b - 1, b - a - 1))
    except:
        exit()
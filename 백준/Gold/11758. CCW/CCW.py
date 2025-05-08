import sys

input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
print(1 if ccw > 0 else -1 if ccw < 0 else 0)
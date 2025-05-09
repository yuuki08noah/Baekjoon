import sys
from functools import cmp_to_key

input = sys.stdin.readline

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def cmp(a, b):
    if ccw(first[:2], a, b) > 0:
        return -1
    elif ccw(first[:2], a, b) < 0:
        return 1
    else:
        da = (a[0] - first[0]) ** 2 + (a[1] - first[1]) ** 2
        db = (b[0] - first[0]) ** 2 + (b[1] - first[1]) ** 2
        if da < db:
            return -1
        elif da > db:
            return 1
t = int(input())
for k in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    points = [(arr[i], arr[i+1], i//2) for i in range(1, 2*n+1, 2)]
    first = min(points, key=lambda p: (p[1], p[0]))
    points.sort(key=cmp_to_key(cmp))
    i = n - 2
    while ccw(first[:2], points[i][:2], points[i+1][:2]) == 0:
        i -= 1
    points[i+1:] = points[i+1:][::-1]
    result = [x[2] for x in points if x != first]
    print(" ".join(map(str, [first[2]] + result)), end='\n' if k != t-1 else '')

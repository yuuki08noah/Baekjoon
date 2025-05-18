import math
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

for i in range(m, 101):
    base = i*(i+1)//2
    if (n - base) % i == 0:
        if math.ceil(n / i) - i // 2 < 0:
            continue
        for j in range(math.ceil(n / i) - i // 2, math.floor(n / i) + i // 2 + 1):
            print(j, end=" ")
        exit()
print(-1)
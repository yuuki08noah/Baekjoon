import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start, end = 0, 10**10
r = 0
def s(v):
    return sum(map(lambda x: x // v, arr))

while start <= end:
    mid = (start + end) // 2
    if s(mid) >= m:
        r = max(r, mid)
        start = mid + 1
    else:
        end = mid - 1
print(r)

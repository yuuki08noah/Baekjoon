import math
import sys

class BIT:
    def __init__(self, size):
        self.n = size + 2
        self.tree = [0] * self.n

    def update(self, i, delta):
        i += 1  # 1-based index
        while i < self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)


input = sys.stdin.readline
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
cnt = 0
results = [0] * q
left, right = queries[0][0]
tree = BIT(200001)

def add(idx):
    global cnt
    val = arr[idx]
    lo = max(0, val - k)
    hi = val + k
    cnt += tree.range_query(lo, hi)
    tree.update(val, 1)


def remove(idx):
    global cnt
    val = arr[idx]
    lo = max(0, val - k)
    hi = val + k
    tree.update(val, -1)
    cnt -= tree.range_query(lo, hi)

for i in range(left, right+1):
    add(i)
results[queries[0][1]] = cnt
start, end = queries[0][0]
for query, idx in queries[1:]:
    left, right = query
    while start > left:
        start -= 1
        add(start)
    while end < right:
        end += 1
        add(end)
    while start < left:
        remove(start)
        start += 1
    while end > right:
        remove(end)
        end -= 1

    results[idx] = cnt
print(*results, sep='\n')
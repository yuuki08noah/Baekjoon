import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, arr):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.build(arr, 1, 1, self.length)

    def merge(self, left, right):
        return left + right

    def merge_range(self, value, length):
        return value * length

    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = arr[start-1]
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.build(arr, node * 2, start, mid)
        right = self.build(arr, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if start >= left and end <= right:
            return self.seg_tree[node]
        mid = (start + end) // 2
        return self.query(node*2, start, mid, left, right) + self.query(node*2+1, mid + 1, end, left, right)

    def update(self, index, value, node, start, end):
        if index < start or end < index:
            return self.seg_tree[node]
        if start == end:
            self.seg_tree[node] += value
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.update(index, value, node * 2, start, mid)
        right = self.update(index, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = [0] * m + [1] * n
    arr = list(map(int, input().split()))
    li = [-1] * (n+1)
    for i in range(1, n+1):
        li[i] = m+i

    s = SegmentTree(l)
    cnt = m
    for j in arr:
        print(s.query(1, 1, n+m, 1, li[j]-1), end=' ')
        s.update(li[j], -1, 1, 1, n+m)
        s.update(cnt, 1, 1, 1, n+m)
        li[j] = cnt
        cnt -= 1
    print()

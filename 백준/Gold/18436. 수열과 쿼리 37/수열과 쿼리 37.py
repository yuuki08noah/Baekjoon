import sys

input = sys.stdin.readline

class SegTree:
    def __init__(self, arr, odd):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.odd = odd
        self.build(arr, 1, 1, self.length)

    def merge(self, left, right):
        return left + right
    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = int(arr[start-1] % 2 == self.odd)
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.build(arr, node * 2, start, mid)
        right = self.build(arr, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]
    def query(self, left, right, node, start, end):
        if right < start or left > end:
            return self.default
        if left <= start and right >= end:
            return self.seg_tree[node]
        mid = (start + end) // 2
        return self.merge(self.query(left, right, node * 2, start, mid), self.query(left, right, node * 2 + 1, mid + 1, end))
    def update(self, index, value, node, start, end):
        if index < start or end < index:
            return self.seg_tree[node]
        if start == end:
            self.seg_tree[node] = int(value % 2 == self.odd)
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.update(index, value, node * 2, start, mid)
        right = self.update(index, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

n = int(input())
arr = list(map(int, input().split()))
st_even = SegTree(arr, 0)
st_odd = SegTree(arr, 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        st_even.update(b, c, 1, 1, n)
        st_odd.update(b, c, 1, 1, n)
    elif a == 2:
        print(st_even.query(b, c, 1, 1, n))
    else:
        print(st_odd.query(b, c, 1, 1, n))

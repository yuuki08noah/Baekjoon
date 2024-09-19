import sys

input = sys.stdin.readline

class SegTree:

    def __init__(self, arr):
        self.default = 1
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.build(arr, 1, 0, self.length - 1)
    def merge(self, left, right):
        return (left * right) % (10**9 + 7)
    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = arr[start]
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
        left_ = self.query(left, right, node * 2, start, mid)
        right_ = self.query(left, right, node * 2 + 1, mid + 1, end)
        return self.merge(left_, right_)
    def update(self, index, value, node, start, end):
        if index < start or end < index:
            return self.seg_tree[node]
        if start == end:
            self.seg_tree[node] = value
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.update(index, value, node * 2, start, mid)
        right = self.update(index, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
tree = SegTree(arr)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b, c, 1, 1, tree.length)
    else:
        print(tree.query(b, c, 1, 1, tree.length))
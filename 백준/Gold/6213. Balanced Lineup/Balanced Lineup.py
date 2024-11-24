# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# sys.setrecursionlimit(10**5)
# arr = [int(input()) for _ in range(n)]
# tree = [0] * (n*4)
# memo = {}
#
# def merge(a, b):
#     return (max(a[0], b[0]), min(a[1], b[1]))
# def build(arr, node, start, end):
#     if start == end:
#         tree[node] = (arr[start], arr[start])
#         return tree[node]
#
#     mid = (start + end) // 2
#     tree[node] = merge(build(arr, node * 2, start, mid), build(arr, node * 2 + 1, mid + 1, end))
#     return tree[node]
#
# def query(node, start, end, left, right):
#     if end < left or start > right:
#         return (0, 10**7)
#     if left <= start and right <= end:
#         return tree[node]
#     mid = (start + end) // 2
#     return merge(query(node * 2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))
#
# build(arr, 1, 0, n - 1)
#
# for i in range(m):
#     x, y = map(lambda k: int(k) - 1, input().split())
#     q = query(1, 0, n - 1, x, y)
#     print(q[0] - q[1])

import sys

input = sys.stdin.readline

class SegTree:

    def __init__(self, arr):
        self.default = 10**9
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.build(arr, 1, 0, self.length - 1)
    def merge(self, left, right):
        return min(left, right)
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
class MaxSegTree(SegTree):
    def __init__(self, arr):
        super().__init__(arr)
        self.default = -10**9

    def merge(self, left, right):
        return max(left, right)

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
minSeg = SegTree(arr)
maxSeg = MaxSegTree(arr)

for i in range(m):
    a, b = map(int, input().split())
    print(maxSeg.query(a, b, 1, 1, minSeg.length) - minSeg.query(a, b, 1, 1, maxSeg.length))

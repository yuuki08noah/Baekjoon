import sys
class SegmentTree:
    def __init__(self, arr):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.build(arr, 1, 1, self.length)
        self.lazy_exist = [False] * (self.length * 4)
        self.lazy_value = [self.default] * (self.length * 4)

    def merge(self, left, right):
        if sum(right) > sum(left) and sum(right) > sum([max(left), max(right)]):
            return right
        elif sum(left) > sum(right) and sum(left) > sum([max(left), max(right)]):
            return left
        return [max(left), max(right)]

    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = [arr[start-1], 0]
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.build(arr, node * 2, start, mid)
        right = self.build(arr, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

    def query(self, left, right, node, start, end):
        mid = (start + end) // 2
        if right < start or left > end:
            return [self.default, self.default]
        if left <= start and right >= end:
            return self.seg_tree[node]

        return self.merge(self.query(left, right, node * 2, start, mid), self.query(left, right, node * 2 + 1, mid + 1, end))

    def update(self, index, value, node, start, end):
        if index < start or end < index:
            return self.seg_tree[node]
        if start == end:
            self.seg_tree[node] = [value, 0]
            return self.seg_tree[node]
        mid = (start + end) // 2
        left = self.update(index, value, node * 2, start, mid)
        right = self.update(index, value, node * 2 + 1, mid + 1, end)
        self.seg_tree[node] = self.merge(left, right)
        return self.seg_tree[node]

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
tree = SegmentTree(arr)
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b, c, 1, 1, n)
    else:
        print(sum(tree.query(b, c, 1, 1, n)))
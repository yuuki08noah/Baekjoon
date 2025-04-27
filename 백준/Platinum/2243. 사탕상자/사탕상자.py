from copy import copy
from typing import List

class Node:
    val: int
    left = None
    right = None
    def __init__(self, value=0):
        self.val = value

class DynamicSegmentTree:
    def merge(self, left, right):
        return left + right

    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.root = Node()
        self.nodes = [self.root]
        self.build(self.root, 1, len(arr)-1, arr)

    def build(self, node, start, end, arr):
        if start > end: return
        if start == end:
            node.val = arr[start]
            return node
        mid = (start + end) // 2
        node.left = self.build(Node(), start, mid, arr)
        node.right = self.build(Node(), mid+1, end, arr)
        node.val = self.merge(node.left.val, node.right.val)
        return node

    def update(self, node, start, end, idx, val):
        if end < idx or idx < start:
            return node
        if start == end:
            node.val += val
            return node
        mid = (start + end) // 2
        if idx <= mid:
            if not node.left:
                node.left = Node()
            node.left = self.update(node.left, start, mid, idx, val)
        else:
            if not node.right:
                node.right = Node()
            node.right = self.update(node.right, mid+1, end, idx, val)

        v1 = node.left.val if node.left else 0
        v2 = node.right.val if node.right else 0
        node.val = self.merge(v1, v2)
        return node

    def query(self, node, start, end, target):
        if not node: return 0
        if start == end: return start
        mid = (start + end) // 2
        left = node.left.val if node.left else 0
        if left >= target:
            return self.query(node.left, start, mid, target)
        return self.query(node.right, mid+1, end, target-left)

n = int(input())
tree = DynamicSegmentTree()
for i in range(n):
    l = list(map(int, input().split()))
    if l[0] == 1:
        k = tree.query(tree.root, 1, 10**6, l[1])
        print(k)
        tree.update(tree.root, 1, 10**6, k, -1)
    else:
        tree.update(tree.root, 1, 10**6, l[1], l[2])

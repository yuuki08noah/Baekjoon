import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class SparseTable:
    input_array = []
    sparse_table = []
    height = 0

    def construct(self, input_array: list):
        self.input_array = input_array
        self.height = math.floor(math.log2(len(input_array)))
        self.sparse_table = [[0]*len(input_array) for _ in range(self.height+1)]
        self.sparse_table[0] = list(range(len(input_array)))

        for i in range(1, self.height+1):
            for j in range(0, len(input_array) - (1 << i) + 1):
                left  = self.sparse_table[i-1][j]
                right = self.sparse_table[i-1][j + (1 << (i-1))]

                self.sparse_table[i][j] = left if self.input_array[left] <= self.input_array[right] else right
        return self.sparse_table

    def range_minimum_query(self, left, right):
        l = right - left + 1
        p = math.floor(math.log2(l))
        i1 = self.sparse_table[p][left]
        i2 = self.sparse_table[p][right - (1 << p) + 1]
        return i1 if self.input_array[i1] <= self.input_array[i2] else i2

n = int(input())
tree = {i: [] for i in range(1, n+1)}
depths = [0] * (n*2-1)
nodes = [0] * (n*2-1)
last = [0] * (n+1)
number = 0
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def visit(node, depth):
    global number
    depths[number] = depth
    nodes[number] = node
    last[node] = number
    number += 1

def dfs(node, depth, parent):
    visit(node, depth)
    for child in tree[node]:
        if child == parent:
            continue
        dfs(child, depth+1, node)
        visit(node, depth)
dfs(1, 0, 0)
depths = depths[:number]
nodes = nodes[:number]
sparse_table = SparseTable()
sparse_table.sparse_table = sparse_table.construct(depths)

def lca(a, b):
    l = min(last[a], last[b])
    r = max(last[a], last[b])

    return sparse_table.range_minimum_query(l, r)

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    print(nodes[lca(a, b)])

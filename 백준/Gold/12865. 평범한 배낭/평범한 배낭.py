import sys
def knapsack(capacity, weight, value, items):
    k = [[0 for _ in range(capacity + 1)] for _ in range(items + 1)]
    for i in range(1, items + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                k[i][w] = max(k[i - 1][w], value[i - 1] + k[i - 1][w - weight[i - 1]])
            else:
                k[i][w] = k[i - 1][w]
    return k[items][capacity]

input = sys.stdin.readline
n, m = map(int, input().split())
weight = []
value = []
for i in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
print(knapsack(m, weight, value, n))
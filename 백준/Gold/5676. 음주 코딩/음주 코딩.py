import sys

input = sys.stdin.readline

segment_tree = [1] * 400000
def merge(a, b):
    return a * b

def to(n):
    if n == 0:
        return 0
    elif n > 0:
        return 1
    else:
        return -1

def build(arr, node, start, end):
    if start == end:
        segment_tree[node] = to(arr[start])
        return segment_tree[node]
    mid = (start + end) // 2
    segment_tree[node] = to(merge(build(arr, node * 2, start, mid), build(arr, node * 2 + 1, mid + 1, end)))
    return segment_tree[node]

def update(node, start, end, index, value):
    if index < start or index > end:
        return segment_tree[node]
    if start == end:
        segment_tree[node] = to(value)
        return segment_tree[node]
    mid = (start + end) // 2
    segment_tree[node] = to(merge(update(node * 2, start, mid, index, value), update(node * 2 + 1, mid + 1, end, index, value)))
    return segment_tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    if start >= left and end <= right:
        return segment_tree[node]

    mid = (start + end) // 2
    return merge(query(node*2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))


while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        build(arr, 1, 0, n - 1)

        for i in range(k):
            op, a, b = input().split()
            a, b = int(a), int(b)
            if op == 'C':
                update(1, 0, n - 1, a-1, b)
            else:
                res = query(1, 0, n - 1, a-1, b-1)
                print('+' if res > 0 else '-' if res < 0 else '0', end='')
        print()
    except:
        break
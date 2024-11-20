import sys

input = sys.stdin.readline

segment_tree = [0] * 2000000
cnt = 0
def merge(left, right):
    sorted = [0] * (len(left)+len(right))
    global cnt
    mid = (len(left) + len(right))//2
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted[k] = left[i]
            i += 1
        else:
            sorted[k] = right[j]
            j += 1
            cnt += len(left) - i
        k += 1

    if j != len(right):
        for l in range(j, len(right)):
            sorted[k] = right[l]
            k += 1
    else:
        for l in range(i, len(left)):
            sorted[k] = left[l]
            k += 1
    return sorted

def build(arr, node, start, end):
    if start == end:
        segment_tree[node] = [arr[start]]
        return segment_tree[node]
    mid = (start + end) // 2
    segment_tree[node] = merge(build(arr, node * 2, start, mid), build(arr, node * 2 + 1, mid + 1, end))
    return segment_tree[node]

n = int(input())
arr = list(map(int, input().split()))
build(arr, 1, 0, n - 1)
# print(segment_tree)
print(cnt)
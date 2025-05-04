import sys
import bisect

input = sys.stdin.readline

class SegTree:
    def __init__(self, arr):
        self.default = 0
        self.length = len(arr)
        self.seg_tree = [0] * (self.length * 4)
        self.arr = arr
        self.build(arr, 1, 0, self.length-1)

    def merge(self, left, right):
        sorted = [0] * (len(left) + len(right))
        mid = (len(left) + len(right)) // 2
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
            k += 1

        for l in range(j, len(right)):
            sorted[k] = right[l]
            k += 1
        for l in range(i, len(left)):
            sorted[k] = left[l]
            k += 1
        return sorted

    def build(self, arr, node, start, end):
        if start == end:
            self.seg_tree[node] = [arr[start]]
            return self.seg_tree[node]
        mid = (start + end) // 2
        self.seg_tree[node] = self.merge(self.build(arr, node * 2, start, mid), self.build(arr, node * 2 + 1, mid + 1, end))
        return self.seg_tree[node]

    def count_more(self, node, start, end, l, r, x):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            # x 보다 큰 수의 개수
            return len(self.seg_tree[node]) - bisect.bisect_right(self.seg_tree[node], x)
        mid = (start + end) // 2
        return (self.count_more(node*2, start, mid, l, r, x) +
                self.count_more(node*2+1, mid+1, end, l, r, x))

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
st = SegTree(arr)
last = 0
for i in range(m):
    a, b, c = map(int, input().split())
    a ^= last
    b ^= last
    c ^= last
    ans = st.count_more(1, 0, n-1, a-1, b-1, c)
    print(ans)
    last = ans
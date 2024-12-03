import sys
import bisect

input = sys.stdin.readline
t = int(input())
# def binary_search(arr, start, end, key):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return start

for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    res = 0
    for item in a:
        bin = bisect.bisect_left(b, item)
        res += bin
    print(res)

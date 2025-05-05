import math
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))

# 쿼리에 인덱스 추가
queries = [(tuple(map(int, input().split())), i) for i in range(q)]
queries.sort(key=lambda x: (x[0][0]//b, x[0][1]))  # right를 직접 비교

# appeared 배열 크기를 arr의 최대 값에 맞춤
max_val = max(arr)
appeared = [0] * (max_val + 1)
cnt = 0
results = [0] * q

def add(x):
    global cnt
    appeared[arr[x]] += 1
    if appeared[arr[x]] == 1:
        cnt += 1

def remove(x):
    global cnt
    appeared[arr[x]] -= 1
    if appeared[arr[x]] == 0:
        cnt -= 1

# 초기 구간 설정
start, end = queries[0][0][0], queries[0][0][0] - 1

for (left, right), idx in queries:
    while start < left:
        remove(start)
        start += 1
    while start > left:
        start -= 1
        add(start)
    while end < right:
        end += 1
        add(end)
    while end > right:
        remove(end)
        end -= 1
    results[idx] = cnt

# 입력 순서대로 출력
for res in results:
    print(res)
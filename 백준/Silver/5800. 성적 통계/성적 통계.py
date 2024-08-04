import sys

input = sys.stdin.readline
t = int(input())
for i in range(1, t+1):
    data = list(map(int, input().split()))
    datas = data[0]
    data.remove(data[0])
    print(f"Class {i}")
    data.sort()
    gap = 0
    for j in range(0, datas-1):
        if data[j+1]-data[j] > gap:
            gap = data[j+1]-data[j]
    print(f"Max {data[-1]}, Min {data[0]}, Largest gap {gap}")


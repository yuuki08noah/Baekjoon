t = int(input())
for _ in range(t):
    import sys
    input = sys.stdin.readline

    n = int(input())
    coins = sorted(list(map(int, input().split())))
    k = int(input())
    arr = [0] * (k+1)
    arr[0] = 1

    for c in coins:
        for i in range(1, k + 1):
            if c <= i:
                arr[i] += arr[i-c]

    print(arr[k])
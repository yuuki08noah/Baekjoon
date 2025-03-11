n = int(input())
arr = [int(input()) for _ in range(n)]
print(sum(arr) - len(arr) + 1)
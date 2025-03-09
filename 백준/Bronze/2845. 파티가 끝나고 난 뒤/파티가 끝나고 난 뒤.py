n, m = map(int, input().split())
print(*list(map(lambda x: int(x) - n*m, input().split())))
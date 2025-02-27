f = lambda x, y: (int(x)+int(y))*(int(x)-int(y))
k = list(map(int, input().split()))
print(f(k[0], k[1]))
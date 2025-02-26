arr = [False for i in range(0, 31)]
for i in range(28):
    arr[int(input())] = True
for i in range(1, 31):
    if not arr[i]: print(i)
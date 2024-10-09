arr = []
for i in range(8):
    arr.append(int(input()))
sor = sorted(arr, reverse=True)
print(sum(sor[:5]))
seq = []
for i in range(5):
    seq.append(arr.index(sor[i])+1)
print(*sorted(seq))
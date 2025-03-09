k = {chr(a): 0 for a in range(ord('a'), ord('z')+1)}
s = input().strip()
for i in s:
    k[i] += 1
for i, v in k.items():
    print(v, end=' ')
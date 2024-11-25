N = int(input())
A = list(map(int, input().split()))
S = int(input())
i = 0
while S > 0 and i < N:
    max_index = A.index(max(A[i:i+S+1]))
    if max_index != i: 
        A[max_index], A[max_index-1] = A[max_index-1], A[max_index]
        S -= 1 
    else:
        i += 1 
print(*A)
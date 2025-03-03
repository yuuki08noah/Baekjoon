for _ in range(int(input())):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    cnt = 0
    for j in arr[1:]:
        if j > avg:
            cnt += 1
    print(f"{(cnt / arr[0])*100:.3f}%")
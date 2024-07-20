import math

def m_m(arr, tp):
    res = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)):
            sum = 0
            for k in range(len(arr[i])):
                sum += tp[i][k] * arr[k][j]
            temp.append(sum%1000)
        res.append(temp)
    return res

def power(base, exponent, t):
    if exponent == 0:
        return t
    elif exponent == 1:
        return base
    elif (exponent % 2) == 1 and exponent > 1:
        temp = power(base, (exponent - 1) // 2, t)
        return m_m(m_m(temp, temp), t) # base * t * t * t
    else:
        temp = power(base, exponent // 2, t)
        return m_m(temp, temp) # ^2

if __name__ == "__main__":
    arr = []
    tp = []
    n, m = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        arr.append(temp)
        tp.append(temp)
    res = power(arr, m, tp)
    for i in res:
        for j in i:
            print(j%1000, end=" ")
        print()
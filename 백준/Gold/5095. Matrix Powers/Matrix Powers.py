import math

def m_m(arr, tp, mod):
    res = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)):
            sum = 0
            for k in range(len(arr[i])):
                sum += tp[i][k] * arr[k][j]
            temp.append(sum%mod)
        res.append(temp)
    return res

def power(base, exponent, t, mod):
    if exponent == 0:
        return t
    elif exponent == 1:
        return base
    elif (exponent % 2) == 1 and exponent > 1:
        temp = power(base, (exponent - 1) // 2, t, mod)
        return m_m(m_m(temp, temp, mod), t, mod) # base * t * t * t
    else:
        temp = power(base, exponent // 2, t, mod)
        return m_m(temp, temp, mod) # ^2

if __name__ == "__main__":
    while True:
        arr = []
        tp = []
        b, mod, p = map(int, input().split())
        if b==0 and p==0 and mod==0: break
        for i in range(b):
            temp = list(map(int, input().split()))
            arr.append(temp)
            tp.append(temp)
        res = power(arr, p, tp, mod)
        for i in res:
            for j in i:
                print(j%mod, end=" ")
            print()
        print()
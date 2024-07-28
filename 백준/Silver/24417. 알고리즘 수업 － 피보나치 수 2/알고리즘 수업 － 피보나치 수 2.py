import math
import sys

def m_m(arr, tp):
    res = []
    for i in range(len(arr)):
        temp = []
        for j in range(len(arr)):
            sum = 0
            for k in range(len(arr[i])):
                sum += tp[i][k] * arr[k][j]
            temp.append(sum%1000000007)
        res.append(temp)
    return res

def power(base, exponent):
    if exponent <= 1:
        return base
    elif (exponent % 2) == 1 and exponent > 1:
        temp = power(base, (exponent - 1) // 2)
        return m_m(m_m(temp, temp), base)
    else:
        temp = power(base, exponent // 2)
        return m_m(temp, temp)

if __name__ == "__main__":
    m = int(sys.stdin.readline())
    arr = [[1, 1], [1, 0]]
    if m==1:
        print(1)
        exit()
    res = power(arr, m)
    print((res[0][1])%1000000007, m-2)
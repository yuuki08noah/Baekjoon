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
            temp.append(sum)
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
    arr = [[1, 1], [1, 0]]
    m = int(sys.stdin.readline())
    if m==0:
        print(0)
        exit()
    res = power(arr, m)
    print(res[0][1])
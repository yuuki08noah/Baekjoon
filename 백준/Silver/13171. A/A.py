import math

def power(base, exponent, c):
    if exponent == 0:
        return 1
    elif exponent % 2:
        temp = power(base, (exponent - 1) // 2, c)
        return (temp * temp * base) % c
    else:
        temp = power(base, exponent // 2, c)
        return (temp * temp) % c

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(power(a, b, 10**9+7))


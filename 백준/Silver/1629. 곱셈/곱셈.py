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
    a, b, c = map(int, input().split())
    print(power(a, b, c))


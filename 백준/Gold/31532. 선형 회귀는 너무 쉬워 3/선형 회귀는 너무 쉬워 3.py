import sys
import math
import cmath


def cubic_function(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def bisection_method(a, b, c, d, lower_bound, upper_bound, tol=1e-6):
    def f(x):
        return cubic_function(a, b, c, d, x)

    if f(lower_bound) * f(upper_bound) >= 0:
        raise ValueError("The bisection method fails. The function values at the endpoints must be of opposite signs.")

    while (upper_bound - lower_bound) / 2.0 > tol:
        midpoint = (lower_bound + upper_bound) / 2.0
        f_mid = f(midpoint)

        if f_mid == 0:
            return midpoint
        elif f(lower_bound) * f_mid < 0:
            upper_bound = midpoint
        else:
            lower_bound = midpoint

    return (lower_bound + upper_bound) / 2.0

input = sys.stdin.readline
n, m = map(int, input().split())
a, b, c, d = 0, 0, 0, 0
for i in range(n):
    t1, t2 = map(int, input().split())
    a += -t1**3
    b += 3*t1**2*(t2-m)
    c += 3*(-t1)*((t2-m)**2)
    d += (t2-m)**3

# 초기 구간 설정
lower_bound = -10
upper_bound = 10

# 실수 해 찾기
try:
    root = bisection_method(a, b, c, d, lower_bound, upper_bound)
    print(root)
except ValueError as e:
    print(e)

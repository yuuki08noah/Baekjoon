def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a, b)
def main():
    n, m = map(int, input().split())

    print(lcm(n, m))


if __name__ == "__main__":
    main()
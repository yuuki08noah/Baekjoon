def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
def main():
    n, m = map(int, input().split())
    for i in range(gcd(n, m)):
        print(1, end="")

if __name__ == "__main__":
    main()
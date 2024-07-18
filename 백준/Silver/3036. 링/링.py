def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
# def lcm(a, b):
#     return a*b//gcd(a, b)
def main():
    t = int(input())
    n = list(map(int, input().split()))
    m = n[0]
    n.pop(0)

    for i in n:
        g = gcd(m, i)
        i //= g
        mm = m//g
        gg = gcd(mm, i)
        i //= gg
        mm //= gg
        print(f'{mm}/{i}')

if __name__ == "__main__":
    main()
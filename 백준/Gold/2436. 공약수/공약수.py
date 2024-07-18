import math

def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a, b)

def main():
    g, l = map(int, input().split())
    min=1000000000000000000000000
    mini, minj=0, 0
    for i in range(1, int(math.sqrt(l//g))+1):
        if((l//g)%i==0 and gcd(i, l//g//i)==1):
            a = i
            b = l//g//a
            if a+b<min:
                mini, minj = a, b

    print(mini*g, minj*g)

if __name__ == "__main__":
    main()
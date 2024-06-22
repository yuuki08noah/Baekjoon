#include <stdio.h>

int gcd(int a, int b) {
    while(b!=0) {
        int t = a;
        a = b;
        b = t % b;
    }
    return a;
}
int lcm(int a, int b) {
    return a*b/(gcd(a, b));
}
int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    printf("%d\n%d\n", gcd(n, m), lcm(n, m));
    
}

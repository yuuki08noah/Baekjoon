#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int gcd(int a, int b) {
    int r;
    while(b!=0) {
        r = a%b;
        a = b;
        b = r;
    }
    return a;
}
int lcm(int a, int b) {
    return (a*b) / gcd(a, b);
}
int main(void) {
    int s1, m1, s2, m2;
    scanf("%d %d %d %d", &s1, &m1, &s2, &m2);
    int l = lcm(m1, m2);
    int d = (s1*(l/m1)+s2*(l/m2));
    int t = gcd(l, d);
    printf("%d %d", d/t, l/t);
}

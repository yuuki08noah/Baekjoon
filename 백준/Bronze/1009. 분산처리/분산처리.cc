#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i<n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        b%=4;
        int num = (int)pow(a%10, b+4);
        num %= 10;
        printf("%d\n", num==0 ? 10 : num);
    }
    return 0;
}

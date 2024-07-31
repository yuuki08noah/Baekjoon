#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, sum=0;
    scanf("%d", &n);
    while(1) {
        sum+=n/5;
        if(n/5==0) break;
        n/=5;
    }
    printf("%d", sum);
}

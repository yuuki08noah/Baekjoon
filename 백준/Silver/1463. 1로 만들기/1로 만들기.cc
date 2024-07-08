#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int d[1000001];
int func(int num) {
    if(num==1) return 0;
    if(d[num]>0) return d[num];
    
    d[num] = func(num-1)+1;
    
    if(num % 3 == 0) {
        int temp = func(num/3)+1;
        if(d[num]>temp) d[num]=temp;
    }
    
    if(num % 2 == 0) {
        int temp = func(num/2)+1;
        if(d[num]>temp) d[num]=temp;
    }
    
    return d[num];
}
int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", func(n));
    return 0;
}

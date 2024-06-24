#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
    return *((int*)a)-*((int*)b);
}
int main(void) {
    int n;
    scanf("%d", &n);
    int num[n];
    for(int i = 0; i<n; i++) {
        scanf("%d", &num[i]);
    }
    qsort(num, n, sizeof(int), compare);
    for(int i = 0; i<n; i++) {
        printf("%d\n", num[i]);
    }
}

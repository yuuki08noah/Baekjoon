#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int compare(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}
int main(void) {
    int n, sum=0;
    scanf("%d", &n);
    int arr[n];
    for(int i = 0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), compare);
    int start = round((double)(n*3)/20);
    int end = n-start;
    
    for(int i = start; i<end; i++) {
        sum+=arr[i];
    }
    printf("%d\n", n ? (int)round((double)sum/(end-start)) : 0);
}

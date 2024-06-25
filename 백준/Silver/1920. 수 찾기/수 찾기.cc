#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void*b) {
    if(*(int*)a > *(int*)b) {
        return 1;
    } else if(*(int*)a < *(int*)b) {
        return -1;
    } else {
        return 0;
    }
}
int f(int arr[], int start, int end, int find) {
    
    int mid = (start+end)/2;
    if(start>end) {
        return 0;
    }
    if(find==arr[0]||find==arr[end]) {
        return 1;
    }
    else if(find>arr[mid]) {
        return f(arr, mid+1, end, find);
    } else if(find<arr[mid]) {
        return f(arr, start, mid-1, find);
    } else if(find==arr[mid]) {
        return 1;
    }
    return 0;
}
int main(void) {
    int n;
    scanf("%d", &n);
    int num[100001];
    for(int i = 0; i<n; i++) {
        scanf("%d", &num[i]);
    }
    
    qsort(num, n, sizeof(int), compare);
    int m;
    scanf("%d", &m);
    for(int i = 0; i<m; i++) {
        int a;
        scanf("%d", &a);
        printf("%d\n", f(num, 0, n-1, a));
    }
}

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void printArr(int arr[], int count) {
    for(int i = 0; i<count; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int shift(int *arr, int count) {
    int pop = 0;
    for(int j = 0; j<count-1; j++) {
//        printArr(arr+pop, count*2-j);
        pop+=2;
        int temp=arr[pop-1];
        arr[count+j]=temp;
    }
    return pop;
}
int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n*2];
    for(int i = 0; i<n; i++) {
        arr[i]=i+1;
    }
    printf("%d\n", arr[shift(arr, n)]);
}

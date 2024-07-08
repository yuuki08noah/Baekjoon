#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MAX_NUM 8001

int ar[MAX_NUM];

int cmp(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    double sum = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
        ar[arr[i] + 4000]++; // -4000부터 4000까지의 수를 0부터 8000 인덱스로 매핑
    }

    qsort(arr, n, sizeof(int), cmp); // 배열 정렬

    // 평균 출력
    printf("%d\n", (int)round(sum / n));

    // 중앙값 출력
    printf("%d\n", arr[n / 2]);

    // 최빈값 출력
    int max_freq = 0;
    int mode = 0;
    int is_second = 0;

    for (int i = 0; i < MAX_NUM; i++) {
        if (ar[i] > max_freq) {
            max_freq = ar[i];
            mode = i - 4000;
            is_second = 0;
        } else if (ar[i] == max_freq && !is_second) {
            mode = i - 4000;
            is_second = 1;
        }
    }
    printf("%d\n", mode);

    // 범위 출력
    printf("%d\n", arr[n - 1] - arr[0]);

    return 0;
}

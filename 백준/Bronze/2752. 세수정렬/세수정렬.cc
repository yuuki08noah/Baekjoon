
#include <stdio.h>
#include <stdlib.h>

int com(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}
int main(void) {
    int a[3];
    scanf("%d %d %d", &a[0], &a[1], &a[2]);
    qsort(a, 3, 4, com);
    printf("%d %d %d", a[0], a[1], a[2]);
}

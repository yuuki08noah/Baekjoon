
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int com(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}
int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    int matrix[n][m];
    for(int i = 0; i<n; i++) {
        for(int j = 0; j<m; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    for(int i = 0; i<n; i++) {
        for(int j = 0; j<m; j++) {
            int p;
            scanf("%d", &p);
            matrix[i][j]+=p;
        }
    }
    for(int i = 0; i<n; i++) {
        for(int j = 0; j<m; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

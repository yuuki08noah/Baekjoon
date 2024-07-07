#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for(int i = 0; i<n; i++) {
        int cents;
        scanf("%d", &cents);
        printf("%d ", cents/25);
        cents%=25;
        printf("%d ", cents/10);
        cents%=10;
        printf("%d ", cents/5);
        cents%=5;
        printf("%d ", cents/1);
        printf("\n");
    }
}

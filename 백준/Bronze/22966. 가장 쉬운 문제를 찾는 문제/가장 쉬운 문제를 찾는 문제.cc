#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int difficulty[n];
    char s[n][11];
    int min = 4;
    int cnt = 0;
    for(int i = 0; i<n; i++) {
        scanf("%s %d", s[i], &difficulty[i]);
    }
    for(int i = 0; i<n; i++) {
        if(difficulty[i] <= min) {
            min = difficulty[i];
            cnt = i;
        }
    }
    
    printf("%s\n", s[cnt]);
}


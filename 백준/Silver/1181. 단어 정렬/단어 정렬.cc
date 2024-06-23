#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int cmpbylen(const void* a, const void*b) {
    return (int)strlen((char*)a) - (int)strlen((char*)b);
}
int cmpbylet(const void* a, const void*b) {
    if((int)strlen((char*)a) == (int)strlen((char*)b)) {
        for(int i = 0; i<51; i++) {
            if(((char*)a)[i]!=((char*)b)[i]) {
                return ((char*)a)[i] - ((char*)b)[i];
                break;
            }
            if(i==strlen((char*)a)-1){
                ((char*)a)[0] = '\0';
                return 0;
            }
        }
    }
    return (int)strlen((char*)a) - (int)strlen((char*)b);
}

int main(void) {
    int n;
    scanf("%d", &n);
    
    char str[n][51];
    for(int i = 0; i<n; i++) {
        fflush(stdin);
        scanf("%s", str[i]);
        str[i][strlen(str[i])] = 0;
    }
    qsort(str, n, 51, cmpbylen);
    qsort(str, n, 51, cmpbylet);
    
    for(int i = 0; i<n; i++) {
        if(str[i][0]!='\0') {
            printf("%s\n", str[i]);
        }
    }
    return 0;
}

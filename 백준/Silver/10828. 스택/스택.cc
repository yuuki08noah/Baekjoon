#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n, num[10000] = {0,};
    scanf("%d", &n);
    int pt = 0;
    for(int i = 0; i<n; i++) {
        char str[10];
        scanf("%s", str);
        if(!strcmp(str, "push")) {
            int m;
            scanf("%d", &m);
            num[pt]+=m;
            pt++;
        } else if(!strcmp(str, "pop")) {
            if(pt==0) {
                printf("-1\n");
                continue;
            }
            pt--;
            printf("%d\n", num[pt]);
            num[pt]=0;
        } else if(!strcmp(str, "size")) {
            int j;
            for(j = 0; num[j]!=0; j++) {}
            printf("%d\n", j);
        } else if(!strcmp(str, "empty")) {
            printf("%d\n", num[0]==0);
        } else if(!strcmp(str, "top")) {
            if(pt==0) {
                printf("-1\n");
                continue;
            }
            printf("%d\n", num[pt-1]);
        }
    }
}
